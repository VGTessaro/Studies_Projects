##PUNCTUATION STRIP
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    for ch in word:
        if ch in punctuation_chars:
            word = word.replace(ch, "")

    return word


# lists of words to use
## POSITIVE ARM
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(st):
    cont_pos = 0
    words = st.split()
    for word in words:
        word = strip_punctuation(word)
        if word in positive_words:
            cont_pos = cont_pos + 1

    return cont_pos


## NEGATIVE ARM
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(st):
    cont_neg = 0
    words = st.split()
    for word in words:
        word = strip_punctuation(word)
        if word in negative_words:
            cont_neg = cont_neg + 1

    return cont_neg


##OUTPUT CSV
output = open("resulting_data.csv", "w")
output.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
output.write("\n")

## TWITTER TEXT
twt = open("twitter_file.txt", "r")
txtlines = twt.readlines()[1:]  # shows lines after header

for lin in txtlines:
    valo = lin.strip().split(",")
    pos_scr = get_pos(lin)
    neg_scr = get_neg(lin)
    net_score = pos_scr - neg_scr

    numb = lin[-1]

    retweet = (valo[1])
    replys = (valo[2])

    write_line = "{},{},{},{},{}".format(retweet, replys, pos_scr, neg_scr, net_score)
    output.write(write_line)
    output.write("\n")

output.close()
