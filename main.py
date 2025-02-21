class BookBot():
    def __init__(self):
        pass    
    def main(self, path_to_file):
        self.path_to_file = path_to_file
        
        with open(path_to_file) as f:
            file_contents = f.read()
        book_string = (str(file_contents))
        return book_string
    
    def count(self, text):
        self.text = text
        count = 0
        words = text.split()
        for word in words:
            count += 1

        return count
    
    def character_count(self, text):
        count_dictionary = {}
        self.text = text
        
        lowered_text = text.lower()
        for char in lowered_text:
            
            if char not in count_dictionary:
                count_dictionary[char] = 1
            else:    
                count_dictionary[char] += 1
        return count_dictionary
    
    def format_report(self, char_counts):
        report_lines = []
        # Sort by count in descending order, then alphabetically by character
        for char, count in sorted(char_counts.items(), key=lambda item: (-item[1], item[0])):
            # Only include alphabetic characters
            if char.isalpha():
                report_lines.append(f"The '{char}' character was found {count} times")
        return "\n".join(report_lines)

    def report(self, book_text):
        # Step 1: Count the words using your existing method
        word_count = self.count(book_text)

        # Step 2: Get the character counts
        char_counts = self.character_count(book_text)

        # Step 3: Format the character counts into a report
        character_report = self.format_report(char_counts)

        # Step 4: Create the top part of the report
        report_header = f"--- Begin report of books/frankenstein.txt ---\n"
        word_count_line = f"{word_count} words found in the document\n"

        # Step 5: Combine all report sections
        full_report = report_header + word_count_line + "\n" + character_report + "\n--- End report ---"

        return full_report
                    
    
bot = BookBot()        
book_text = bot.main("books/frankenstein.txt")
word_count = bot.count(book_text)
dictionary = bot.character_count(book_text)
report_franken = bot.report(book_text)

print(report_franken)