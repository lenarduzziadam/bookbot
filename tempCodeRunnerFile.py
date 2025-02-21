     lowered_text = book_text.lower()

        # Use your first function to get character counts
        char_counts = self.count_characters(lowered_text)

        # Use your second function to build the report
        report_output = self.format_report(char_counts)

        # Return or print the formatted report
        return report_output