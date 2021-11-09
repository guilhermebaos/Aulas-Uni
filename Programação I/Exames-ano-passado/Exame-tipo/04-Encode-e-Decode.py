def encode(d: dict, x: str):
    message = ''
    for letter in x:
        message += d[letter]
    return message


my_res1 = encode({'A': 'GvpmBf', 'B': 'KzUcdjpz', 'C': 'rWIss', 'D': 'mtlVHMe', 'E': 'HAtRDiM', 'F': 'QNUJzQQ', 'G': 'tGDtohA', 'H': 'UqeHS', 'I': 'BUEsBFU', 'J': 'CZOB', 'K': 'kvLVrN', 'L': 'FrLCmWS', 'M': 'yMHMb', 'N': 'qyGasZz', 'O': 'TZYs', 'P': 'TUMbIksc', 'Q': 'dtuyWnva', 'R': 'vNGwuMp', 'S': 'uGifcwF', 'T': 'pkOewj', 'U': 'LigSFPgj', 'V': 'UdnothU', 'W': 'JehpH', 'X': 'algBgtsQ', 'Y': 'fEOkDJ', 'Z': 'XixTZj', ' ': 'YXzNAYAC'}, 'JX IKQNY JSLHBPLLP  L GPMXUYZV ISYE  K R OY L   PO')
res1 = 'CZOBalgBgtsQYXzNAYACBUEsBFUkvLVrNdtuyWnvaqyGasZzfEOkDJYXzNAYACCZOBuGifcwFFrLCmWSUqeHSKzUcdjpzTUMbIkscFrLCmWSFrLCmWSTUMbIkscYXzNAYACYXzNAYACFrLCmWSYXzNAYACtGDtohATUMbIkscyMHMbalgBgtsQLigSFPgjfEOkDJXixTZjUdnothUYXzNAYACBUEsBFUuGifcwFfEOkDJHAtRDiMYXzNAYACYXzNAYACkvLVrNYXzNAYACvNGwuMpYXzNAYACTZYsfEOkDJYXzNAYACFrLCmWSYXzNAYACYXzNAYACYXzNAYACTUMbIkscTZYs'
print(res1 == my_res1)

my_res2 = encode({'A': 'kyvtOfK', 'B': 'dqNjquG', 'C': 'zGnazgDI', 'D': 'gswgRzH', 'E': 'sOENJl', 'F': 'pNICj', 'G': 'KBHpeiBZ', 'H': 'diWlzH', 'I': 'ZAKyL', 'J': 'WKIlRny', 'K': 'TSvjoSI', 'L': 'uMAkRPU', 'M': 'agmyAMan', 'N': 'XmJF', 'O': 'AgmS', 'P': 'wQGwtD', 'Q': 'PXxRNjj', 'R': 'aXxvmLc', 'S': 'hyiSJu', 'T': 'DjKP', 'U': 'ilSxklwl', 'V': 'CFwgcBtz', 'W': 'GqpUf', 'X': 'DFdDrBfa', 'Y': 'Bzccorh', 'Z': 'NuroPJj', ' ': 'DeOFbCIA'}, '      CAZEBDK HA  MLR A RWH B   Y HWQ  G  SN QG  E')
res2 = 'DeOFbCIADeOFbCIADeOFbCIADeOFbCIADeOFbCIADeOFbCIAzGnazgDIkyvtOfKNuroPJjsOENJldqNjquGgswgRzHTSvjoSIDeOFbCIAdiWlzHkyvtOfKDeOFbCIADeOFbCIAagmyAManuMAkRPUaXxvmLcDeOFbCIAkyvtOfKDeOFbCIAaXxvmLcGqpUfdiWlzHDeOFbCIAdqNjquGDeOFbCIADeOFbCIADeOFbCIABzccorhDeOFbCIAdiWlzHGqpUfPXxRNjjDeOFbCIADeOFbCIAKBHpeiBZDeOFbCIADeOFbCIAhyiSJuXmJFDeOFbCIAPXxRNjjKBHpeiBZDeOFbCIADeOFbCIAsOENJl'
print(res2 == my_res2)


def decode(d: dict, y: str):
    message = ''
    keys, values = [], []
    for key, value in zip(d.keys(), d.values()):
        keys += [key]
        values += [value]

    start, end = 0, 1
    len_y = len(y)
    while True:
        sub_str = y[start:end]
        if sub_str in values:
            message += keys[values.index(sub_str)]
            start = end
        end += 1
        if end > len_y + 1:
            break

    return message


my_res1 = decode({'A': 'KoBAXD', 'B': 'WfZc', 'C': 'Lzss', 'D': 'nZGzrFbJ', 'E': 'tSKvEG', 'F': 'cVNIE', 'G': 'cHBpzXoC',
        'H': 'OGEByl', 'I': 'IBhR', 'J': 'ogqKsORI', 'K': 'AKGOvj', 'L': 'hVNXc', 'M': 'fRbnK', 'N': 'dHBbHQp',
        'O': 'DEJSDUei', 'P': 'EvDCDp', 'Q': 'GkFd', 'R': 'SgDSauY', 'S': 'cLtX', 'T': 'uQxHxZ', 'U': 'mJma',
        'V': 'cMzGaz', 'W': 'pUdeqzW', 'X': 'tSYFfXy', 'Y': 'IldZcc', 'Z': 'JAtBgXAH', ' ': 'QUxHIYWW'},
       'QUxHIYWWuQxHxZcHBpzXoCEvDCDpIBhRtSKvEGdHBbHQpAKGOvjGkFdGkFdQUxHIYWWQUxHIYWWIldZcchVNXcQUxHIYWWpUdeqzWpUdeqzWQUxHIYWWcHBpzXoCQUxHIYWWWfZcQUxHIYWWfRbnKQUxHIYWWcMzGazDEJSDUeiAKGOvjSgDSauYtSKvEGIldZccOGEBylIBhRtSYFfXyQUxHIYWWIldZcccMzGazQUxHIYWWogqKsORItSKvEGQUxHIYWWtSYFfXyGkFddHBbHQpWfZccLtXQUxHIYWWAKGOvjQUxHIYWWQUxHIYWWQUxHIYWW')
res1 = ' TGPIENKQQ  YL WW G B M VOKREYHIX YV JE XQNBS K   '
print(res1 == my_res1)

my_res2 = decode({'A': 'qniM', 'B': 'uGGFZJm', 'C': 'fmWL', 'D': 'SKYoPS', 'E': 'OAbGqg', 'F': 'MhZMz', 'G': 'ikVUx', 'H': 'VhSLv', 'I': 'copWYtrB', 'J': 'TQoCypw', 'K': 'eMlHOC', 'L': 'zozk', 'M': 'HTzh', 'N': 'RpBcpe', 'O': 'PARVPkNy', 'P': 'BdzIfH', 'Q': 'qkbKAng', 'R': 'vQvaE', 'S': 'lLTkkAQS', 'T': 'oadM', 'U': 'brhptqD', 'V': 'zWOum', 'W': 'OYOtDqY', 'X': 'mVwvuFaT', 'Y': 'wCsQd', 'Z': 'EflwWWrc', ' ': 'zzYOyhv'}, 'uGGFZJmeMlHOCTQoCypweMlHOCzzYOyhvEflwWWrcSKYoPSTQoCypwOYOtDqYzWOumzzYOyhvSKYoPSoadMOYOtDqYcopWYtrBPARVPkNyzzYOyhvoadMzozkzzYOyhvOAbGqgikVUxOYOtDqYzzYOyhvMhZMzzzYOyhvzzYOyhvzzYOyhvqniMzWOumqkbKAngTQoCypwwCsQdEflwWWrczzYOyhvSKYoPSzzYOyhvRpBcpelLTkkAQSRpBcpeSKYoPSfmWLcopWYtrBbrhptqDPARVPkNyzWOumlLTkkAQSRpBcpezzYOyhvBdzIfH')
res2 = 'BKJK ZDJWV DTWIO TL EGW F   AVQJYZ D NSNDCIUOVSN P'
print(res2 == my_res2)