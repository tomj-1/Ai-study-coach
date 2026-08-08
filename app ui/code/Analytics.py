class Analytics:

    def accuracy_by_topics(self,results):
        topic_data = {}

        for result in results:
            topic = result["topic"]
            grade = result["grade"]

            if topic not in topic_data:
                topic_data[topic] = []

            topic_data[topic].append(grade)
    

        for topic in topic_data:
            topic_data[topic] = (
                sum(topic_data[topic]) / len(topic_data[topic])
            ) * 100

        return topic_data

    def overall_accuracy(self, results):
        if len(results) == 0:
            return 0

        total = 0

        for result in results:
            if result["grade"] == 100:
                result["grade"] = 1
            total += result["grade"]
            

        return (total / len(results)) * 100

