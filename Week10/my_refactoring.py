"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""

def count_keyword(filename, lines, keyword):
    """
    Count number of loops in the program
    :param lines: list of lines in the program
    :param keyword: keyword to count
    :return: number of loops
    """

    num_loops = 0

    for line in lines:
        if line.strip().startswith(keyword):
            num_loops += 1

    print(f'Program {filename} contain {num_loops} {keyword} loops')

def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """

    filename = input("Enter program filename: ")
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    count_keyword(filename, lines, "for")
    count_keyword(filename, lines, "while")
    count_keyword(filename, lines, "if")
