from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num



from flask import redirect

PER_PAGE = 20

@app.route('/files/', defaults={'page': 1})
@app.route('/files/file/<int:page>')
def download_file(page):
    count = count_all_downloader() # add logic to count how many files to download
    downloader = get_users_for_page(page, PER_PAGE, count)
    if not users and page != 1:
        abort(404)
    pagination = Pagination(page, PER_PAGE, count)
    return 

@app.route('/downloadResult') # should be timestamp, if too large return json, if not too large return zip file
def download_files():
    mypath = './local_files'
    resultFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9666)