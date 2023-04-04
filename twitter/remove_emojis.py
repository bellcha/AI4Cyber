import demoji
 
with open('ai4cyber_hacked_tweets.csv', 'r') as r:
    lines = r.read().splitlines()

    with open('ai4cyber_hacked_tweets_noemojis.csv', 'w') as ne:

        for line in lines:
            ne.write(f'{demoji.replace_with_desc(line)}\n')