import web 
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
class hello:
    def GIT(self, nme):
        return open(r'web.py.html','r').read()
if __name__ == "__main__":
    app.run()
