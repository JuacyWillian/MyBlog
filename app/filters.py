def reverse_filter(s):
    return s[::-1]


def configure(app):
    app.jinja_env.filters['reverse'] = reverse_filter
