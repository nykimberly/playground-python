class AnonPoll():
    """Poll users anonymously and collect answers."""
        
    def __init__(self, question):
        """Initialize a question for the poll and empty response list"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question"""
        return self.question

    def store_response(self, new_response):
        """Store a new response to the list"""
        self.responses.append(new_response)

    def show_results(self):
        """Print results to the question"""
        count = 1
        print("Poll Results: ")
        for response in self.responses:
            print("\t" + str(count) + ". " + response)
            count += 1
