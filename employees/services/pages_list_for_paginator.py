def get_pages_list_for_paginator(context):
    paginator = context.get('paginator')
    num_pages = paginator.num_pages
    current_page = context.get('page_obj')
    page_no = current_page.number
    if num_pages <= 11 or page_no <= 6:
        pages = [x for x in range(1, min(num_pages + 1, 12))]
    elif page_no > num_pages - 6:
        pages = [x for x in range(num_pages - 10, num_pages + 1)]
    else:
        pages = [x for x in range(page_no - 5, page_no + 6)]
    return pages