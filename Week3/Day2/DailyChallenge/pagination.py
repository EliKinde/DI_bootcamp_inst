'''class Pagination:
    def __init__(self, items, pageSize):
        self.items = items
        self.pageSize = pageSize

    def getVisibleItems(self):
        print(len(self.items))

    def prePage(self):
        pass

    def nextPage(self):
        pass

    def firstPage(self):
        pass

    def lastPage(self):
        pass

    def goToPage(self):
        pass


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

page = Pagination(alphabetList, 4)

page.getVisibleItems()'''

class Paginator:
    def __init__(self, items, items_per_page):
        """
        Initialize the Paginator with items and items per page.

        :param items: List of items to be paginated
        :param items_per_page: Number of items per page
        """
        self.items = items
        self.items_per_page = items_per_page
        self.total_items = len(items)
        self.total_pages = (self.total_items + items_per_page - 1) // items_per_page
        self.current_page = 3

    def get_page(self, page_number):
        """
        Get the items for a specific page.

        :param page_number: The page number to retrieve
        :return: List of items for the specified page
        """
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("Page number out of range.")

        start_index = (page_number - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.items[start_index:end_index]

    def set_page(self, page_number):
        """
        Set the current page.

        :param page_number: The page number to set as current
        """
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("Page number out of range.")
        self.current_page = page_number

    def next_page(self):
        """
        Move to the next page.

        :return: List of items for the next page, or None if already on the last page
        """
        if self.current_page < self.total_pages:
            self.current_page += 1
            return self.get_page(self.current_page)
        return None

    def previous_page(self):
        """
        Move to the previous page.

        :return: List of items for the previous page, or None if already on the first page
        """
        if self.current_page > 1:
            self.current_page -= 1
            return self.get_page(self.current_page)
        return None

    def get_current_page(self):
        """
        Get the items for the current page.

        :return: List of items for the current page
        """
        return self.get_page(self.current_page)

    def __str__(self):
        return (f"Page {self.current_page} of {self.total_pages}\n"
                f"Items: {self.get_current_page()}")

# Example Usage

items = list("abcdefghijklmnopqrstuvwxyz")
#items = list(range(1, 101))  # A list of 100 items
paginator = Paginator(items, 4)  # 10 items per page

#print(paginator)  # Show the current page (1)
#print(paginator.next_page())  # Move to page 2 and show items
paginator.set_page(int(input("Enter the page that you want: ")))  # Set to page 5
print(paginator.get_current_page())  # Show items on page 5
print(paginator.previous_page())  # Move back to page 4 and show items
print(paginator.next_page())  # Move to page 2 and show items
print(paginator.next_page())  # Move to page 2 and show items

