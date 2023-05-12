import math

import numpy as np


def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)[:k]
    recommended_list = np.array(recommended_list)[:k]

    is_buy = np.isin(recommended_list, bought_list)

    return is_buy.sum() / len(recommended_list)


def money_recall_at_k(recommended_list, bought_list, prices, k=5):
    bought_list = np.array(bought_list)[:k]
    recommended_list = np.array(recommended_list)[:k]
    prices_recommended = []
    prices_bought = []
    for each in bought_list:
        prices_bought.append(prices[each])
    for each in recommended_list:
        prices_recommended.append(prices[each])

    prices_bought = np.array(prices_bought)
    prices_recommended = np.array(prices_recommended)
    print(prices_bought, prices_recommended)
    return prices_bought.sum()/prices_recommended.sum()


def mrr_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)[:k]
    recommended_list = np.array(recommended_list)[:k]
    min_rank = np.inf
    print(bought_list, recommended_list)
    for el_bought in bought_list:
        el = np.where(recommended_list == el_bought)
        if min_rank > el[0].min():
            min_rank = el[0].min()
    if min_rank == np.inf:
            MMR = 0
    else:
        MMR = 1/(min_rank+1)
    return MMR


def ndcg_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)[:k]
    recommended_list = np.array(recommended_list)[:k]

    is_buy = np.isin(recommended_list, bought_list)
    DCG = 0
    IDCG = 0
    for i in range(len(is_buy)):
        if is_buy[i]:
            DCG += 1 / math.log2(i + 2)
    for i in range(len(bought_list)):
        IDCG += 1 / math.log2(i + 2)
    return DCG / IDCG


def hit_rate(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)
    hit_rate = int(flags.sum() > 0)

    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list[:k], bought_list, )
    hit_rate = int(flags.sum() > 0)

    return hit_rate


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = (flags * prices_recommended).sum() / prices_recommended.sum()

    return precision


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(k):

        if flags[i]:
            p_k = precision_at_k(recommended_list, bought_list, k=i + 1)
            sum_ += p_k

    result = sum_ / k

    return result

