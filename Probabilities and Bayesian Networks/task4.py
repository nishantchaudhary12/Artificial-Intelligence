import sys

def probability(argv):

    file = argv[1]
    # print(file)
    ip = open(file, 'r')
    cost = 0
    # data = list()

    baseball_game_on_TV = 0
    George_watches_TV = 0
    out_of_cat_food = 0
    George_feeds_cat = 0

    G_watches_TV_Baseball_on_Tv = 0
    G_watches_TV_No_Baseball_on_Tv = 0

    G_feeds_cat_No_cat_food_watches_TV = 0
    G_feeds_cat_Cat_food_dont_watch_TV = 0

    G_feeds_cat_No_cat_food_dont_watch_TV = 0
    G_feeds_cat_Cat_food_watches_TV = 0

    no_cat_food_watches_TV = 0
    no_cat_food_dont_watch_TV = 0

    cat_food_watches_TV = 0
    cat_food_dont_watch_TV = 0

    G_dont_feed_game_on_TV = 0


    # print(ip)
    for each in ip:
        cost = cost + 1
        data = list(each.strip().replace(" ", ""))
        # print(data)

        if data[0] == '1':
            baseball_game_on_TV += 1
        if data[1] == '1':
            George_watches_TV += 1
        if data[2] == '1':
            out_of_cat_food += 1
        if data[3] == '1':
            George_feeds_cat += 1

        if data[0] == '1' and data[1] == '1':
            G_watches_TV_Baseball_on_Tv += 1
        if data[0] == '0' and data[1] == '1':
            G_watches_TV_No_Baseball_on_Tv += 1
        if data[1] == '1' and data[2] == '1' and data[3] == '1':
            G_feeds_cat_No_cat_food_watches_TV += 1
        if data[1] == '1' and data[2] == '0' and data[3] == '1':
            G_feeds_cat_Cat_food_watches_TV += 1
        if data[1] == '1' and data[2] == '1':
            no_cat_food_watches_TV += 1
        if data[1] == '1' and data[2] == '0':
            cat_food_watches_TV += 1
        if data[1] == '0' and data[2] == '1' and data[3] == '1':
            G_feeds_cat_No_cat_food_dont_watch_TV += 1
        if data[1] == '0' and data[2] == '0' and data[3] == '1':
            G_feeds_cat_Cat_food_dont_watch_TV += 1
        # if data[1] == '0' and data[2] == '1' and data[3] == '1':
        #     G_feeds_cat_No_cat_food_dont_watch_TV += 1
        if data[2] == '1' and data[1] == '0':
            no_cat_food_dont_watch_TV += 1
        if data[2] == '0' and data[1] == '0':
            cat_food_dont_watch_TV += 1

        if data[3] == '0' and data[0] == '1':
            G_dont_feed_game_on_TV += 1

    not_baseball_game_on_TV = 365 - baseball_game_on_TV
    probability_baseball = baseball_game_on_TV / cost
    probability_feedsCat_noFood_watchesTV = G_feeds_cat_No_cat_food_watches_TV / no_cat_food_watches_TV
    probability_feedsCat_Food_watchesTV = G_feeds_cat_Cat_food_watches_TV / cat_food_watches_TV
    probability_baseballGame_watchesTV = G_watches_TV_Baseball_on_Tv / baseball_game_on_TV
    probability_notbaseballGame_watchesTV = G_watches_TV_No_Baseball_on_Tv / not_baseball_game_on_TV
    probability_notwatchesTV_feedsCat_catFood = G_feeds_cat_Cat_food_dont_watch_TV / cat_food_dont_watch_TV
    probability_notwatchesTV_feedsCat_notcatFood = G_feeds_cat_No_cat_food_dont_watch_TV / no_cat_food_dont_watch_TV
    probability_notCatFood = out_of_cat_food / cost


    print('\n')
    print('Table for baseball_game_on_TV')
    print('Probability for baseball game on TV', probability_baseball)

    print('\n')
    print('Table for out of cat food')
    print('Probability out of cat food', probability_notCatFood)

    print('\n')
    print('Table for George watches TV')
    print('Probability for George watches TV and baseball game on TV', probability_baseballGame_watchesTV)
    print('Probability for George watches TV and baseball game not on TV', probability_notbaseballGame_watchesTV)

    print('\n')
    print('Table for George Feeds Cat')
    print('Probability for George feeds cat and not out of cat food and George watches TV', probability_feedsCat_Food_watchesTV)
    print('Probability for George feeds cat and out of cat food and George watches TV', probability_feedsCat_noFood_watchesTV)
    print('Probability for George feeds cat and not out of cat food and George does not watch TV', probability_notwatchesTV_feedsCat_catFood)
    print('Probability for George feeds cat and out of cat food and George does not watch TV', probability_notwatchesTV_feedsCat_notcatFood)


if __name__ == '__main__':
    probability(sys.argv)


