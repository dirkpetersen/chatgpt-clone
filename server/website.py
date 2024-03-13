import os, time
import flask  

class Website:
    def __init__(self, app) -> None:
        self.app = app
        self.routes = {
            '/': {
                'function': lambda: flask.redirect('/chat'),
                'methods': ['GET', 'POST']
            },
            '/chat/': {
                'function': self._index,
                'methods': ['GET', 'POST']
            },
            '/chat/<conversation_id>': {
                'function': self._chat,
                'methods': ['GET', 'POST']
            },
            '/assets/<folder>/<file>': {
                'function': self._assets,
                'methods': ['GET', 'POST']
            }
        }

    def _chat(self, conversation_id):
        if not '-' in conversation_id:
            return flask.redirect(f'/chat')

        return flask.render_template('index.html', chat_id=conversation_id)

    def _index(self):
        return flask.render_template('index.html', chat_id=f'{os.urandom(4).hex()}-{os.urandom(2).hex()}-{os.urandom(2).hex()}-{os.urandom(2).hex()}-{hex(int(time.time() * 1000))[2:]}')

    def _assets(self, folder: str, file: str):
        try:
            return flask.send_file(f"./../client/{folder}/{file}", as_attachment=False)
        except:
            return "File not found", 404
