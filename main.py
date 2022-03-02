def _bulid_result_line(sentence, tag_pred):
    result_list = []
    for index, tag in zip(range(len(tag_pred)), tag_pred):
        if tag[0] == 'B':
            start = index
            end = index
            label_type = tag[2:]
            if end != len(tag_pred) - 1:
                while tag_pred[end + 1][0] == 'I' and tag_pred[end + 1][2:] == label_type:
                    end += 1
                    if end == len(tag_pred) - 1:
                        break
            result_list.append({'start': start,
                                'end': end,
                                'lable_type': label_type

                                })
    nouns = []
    line = ''.join(sentence)
    if len(result_list) != 0:
        for index, item in enumerate(result_list):
            nouns.append(''.join(sentence[result_list[index]['start']:result_list[index]['end'] + 1]))
    return nouns


text = ['4', '到', '8', '元', '板', '块', '龙', '头', '股', '，', 's', 't', '除', '外', '，', '3', '日', '缩', '量', '庄', '家', '抬',
        '桥']
tags = ['O', 'O', 'O', 'O', 'B-NOUN', 'I-NOUN', 'I-NOUN', 'I-NOUN', 'I-NOUN', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'B-NOUN', 'I-NOUN', 'I-NOUN', 'I-NOUN']
print(_bulid_result_line(text, tags))
