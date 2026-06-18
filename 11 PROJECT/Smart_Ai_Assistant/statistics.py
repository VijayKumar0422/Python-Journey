import json


def load_stats():

    try:

        with open("data/stats.json", "r") as file:

            return json.load(file)

    except:

        return {
            "total_questions": 0,
            "known_questions": 0,
            "unknown_questions": 0
        }


def save_stats(stats):

    with open("data/stats.json", "w") as file:

        json.dump(stats, file, indent=4)


def update_stats(is_known):

    stats = load_stats()

    stats["total_questions"] += 1

    if is_known:

        stats["known_questions"] += 1

    else:

        stats["unknown_questions"] += 1

    save_stats(stats)


def show_stats():

    stats = load_stats()

    print("\nStatistics")

    print("Total Questions :", stats["total_questions"])

    print("Known Questions :", stats["known_questions"])

    print("Unknown Questions :", stats["unknown_questions"])