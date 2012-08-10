import wsgiref.handlers
import webapp2

import base
import handlers.browse
import handlers.async
from admin import post
from admin import usr
from admin import siteconf
from admin import comments
import rss
import sitemap

if __name__ == '__main__':
    application = webapp2.WSGIApplication([
        ('/', handlers.browse.Index),
        ('/post_tags', handlers.async.Tags),
        ('/json/loadcomments', handlers.async.CommentsLoader),
        ('/json/leavecomment', handlers.async.CommentRecv),
        ('/c/newpost', post.NewPost),
        ('/c/preview', post.Preview),
        ('/c/add', post.Add),
        ('/c/posts', post.List),
        ('/c/edit', post.Edit),
        ('/c/comments', comments.List),
        ('/c/pendingcomments', comments.ListPending),
        ('/c/delcomment', comments.Delete),
        ('/c/approvecomment', comments.Approve),
        ('/c/clearpending', comments.ClearPending),
        ('/c/reg', usr.Register),
        ('/c/newusr', usr.New),
        ('/c/login', usr.LoginPage),
        ('/c/auth', usr.LoginAction),
        ('/c/siteconf', base.page_renderer('templates/siteconf.html')),
        ('/c/savesiteconf', siteconf.Save),
        ('/about', base.page_renderer('templates/about.html')),
        ('/rss', rss.Build),
        ('/sitemap.*', sitemap.Build),
        ('/.*', base.NotFound),
    ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)
