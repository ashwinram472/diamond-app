def parse_arguments():
    parser = argparse.ArgumentParser()

    shapes = [
        "RD",  # round
        "PR",  # princess
        "EC",  # emerald
        "AS",  # asscher
        "CU",  # cushion
        "MQ",  # marquise
        "RA",  # radiant
        "OV",  # oval
        "PS",  # pear
        "HS",  # heart
    ]
    parser.add_argument('--shape', nargs='+', choices=shapes)

    parser.add_argument('--minPrice', type=int)
    parser.add_argument('--maxPrice', type=int)
    parser.add_argument('--minCarat', type=float)
    parser.add_argument('--maxCarat', type=float)

    cuts = ['Good', 'Very Good', 'Ideal', 'Signature Ideal']
    colors = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    clarities = ['SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']
    select_one = [
        ('minCut', cuts),
        ('maxCut', cuts),
        ('minColor', colors),
        ('maxColor', colors),
        ('minClarity', clarities),
        ('maxClarity', clarities),
    ]
    for key, choices in select_one:
        parser.add_argument('--%s' % key, choices=choices)

    arguments_with_defaults = [
        ('startIndex', 0),
        ('pageSize', 1000),
        ('country', 'USA'),
        ('language', 'en-us'),
        ('currency', 'USD'),
        ('sortColumn', 'price'),
        ('sortDirection', 'asc'),
    ]
    for k, v in arguments_with_defaults:
        parser.add_argument('--%s' % k, default=v, type=type(v))

    args = parser.parse_args()
    d = args.__dict__
    for k, v in list(d.items()):
        if v is None:
            del d[k]
    return d