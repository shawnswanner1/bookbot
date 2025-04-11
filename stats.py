def get_num_words(booktext):
    return len(booktext.split())

def get_letter_counts(booktext):
    counts = {}
    for i in range(0, len(booktext) - 1):
        if booktext[i].lower() in counts:
            counts[booktext[i].lower()] += 1
        else:
            counts[booktext[i].lower()] = 1
    return counts

def get_report(counts):
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
