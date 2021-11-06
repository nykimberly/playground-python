"""
You are given an HTML code snippet of  lines.
Your task is to print start tags, end tags and empty tags separately.

Format your results in the following way:
    Start : Tag1
    End   : Tag1
    Start : Tag2
    -> Attribute2[0] > Attribute_value2[0]
    -> Attribute2[1] > Attribute_value2[1]
    -> Attribute2[2] > Attribute_value2[2]
    Start : Tag3
    -> Attribute3[0] > None
    Empty : Tag4
    -> Attribute4[0] > Attribute_value4[0]
    End   : Tag3
    End   : Tag2

"""


if __name__ == '__main__':

    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            if attrs is not None:
                for attr in attrs:
                    print("->", attr[0], ">", attr[1])

        def handle_endtag(self, tag):
            print("Empty :", tag)

        def handle_startendtag(self, tag, attrs):
            print("End :", tag)

    parser = MyHTMLParser()
    N = input()
    for _ in range(int(N)):
        parser.feed(input())
