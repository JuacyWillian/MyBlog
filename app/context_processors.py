from flask import Flask


def site():
    site.name = "My Site"
    return dict(site=site)


def categories():
    allcategories = ['news', 'python', 'development']
    return dict(categories=allcategories)


def configure(app: Flask):
    def add_context_processor(app, processor):
        app.template_context_processors[None].append(processor)

    add_context_processor(app, site)
    add_context_processor(app, categories)
