import re

class custom_regex:
    def __init__(self):
        self.response = ''
    
    def remove_diacritics(origText):
        origText = re.sub('[áăắặằẳẵǎâấậầẩẫäǟȧǡạȁàảȃāąåǻḁⱥã]', 'a', origText)
        origText = re.sub('[ÁĂẮẶẰẲẴǍÂẤẬẦẨẪÄǞȦǠẠȀÀẢȂĀĄÅǺḀȺÃ]', 'A', origText)
        origText = re.sub('[ḃḅɓḇƀƃ]', 'b', origText)
        origText = re.sub('[ḂḄƁḆɃƂ]', 'B', origText)
        origText = re.sub('[ćčḉçĉċƈȼ]', 'c', origText)
        origText = re.sub('[ĆČḈÇĈĊƇȻ]', 'C', origText)
        origText = re.sub('[ďḑḓḋḍɗḏđƌǳǆ]', 'd', origText)
        origText = re.sub('[ĎḐḒḊḌƊḎǲǅĐƋǱǄ]', 'D', origText)
        origText = re.sub('[éĕěȩḝêếệềểễḙëėẹȅèẻȇēḗḕęɇẽḛ]', 'e', origText)
        origText = re.sub('[ÉĔĚȨḜÊẾỆỀỂỄḘËĖẸȄÈẺȆĒḖḔĘɆẼḚ]', 'E', origText)
        origText = re.sub('[ḟƒ]', 'f', origText)
        origText = re.sub('[ḞƑ]', 'F', origText)
        origText = re.sub('[ǵğǧģĝġɠḡǥ]', 'g', origText)
        origText = re.sub('[ǴĞǦĢĜĠƓḠǤ]', 'G', origText)
        origText = re.sub('[ḫȟḩĥⱨḧḣḥħ]', 'h', origText)
        origText = re.sub('[ḪȞḨĤⱧḦḢḤĦ]', 'H', origText)
        origText = re.sub('[ıíĭǐîïḯịȉìỉȋīįɨĩḭ]', 'i', origText)
        origText = re.sub('[ÍĬǏÎÏḮİỊȈÌỈȊĪĮƗĨḬ]', 'I', origText)
        origText = re.sub('[ǰĵɉ]', 'j', origText)
        origText = re.sub('[ĴɈ]', 'J', origText)
        origText = re.sub('[ḱǩķⱪḳƙḵ]', 'k', origText)
        origText = re.sub('[ḰǨĶⱩḲƘḴ]', 'K', origText)
        origText = re.sub('[ĺƚľļḽḷḹⱡḻŀł]', 'l', origText)
        origText = re.sub('[ĹȽĽĻḼḶḸⱠḺĿǈŁ]', 'L', origText)
        origText = re.sub('[ḿṁṃ]', 'm', origText)
        origText = re.sub('[ḾṀṂ]', 'M', origText)
        origText = re.sub('[ńňņṋṅṇǹɲṉƞñ]', 'n', origText)
        origText = re.sub('[ŃŇŅṊṄṆǸƝṈȠǋÑ]', 'N', origText)
        origText = re.sub('[óŏǒôốộồổỗöȫȯȱọőȍòỏơớợờởỡȏōṓṑǫǭøǿõṍṏȭ]', 'o', origText)
        origText = re.sub('[ÓŎǑÔỐỘỒỔỖÖȪȮȰỌŐȌÒỎƠỚỢỜỞỠȎŌṒṐǪǬØǾÕṌṎȬ]', 'O', origText)
        origText = re.sub('[ṕṗƥᵽ]', 'p', origText)
        origText = re.sub('[ṔṖƤⱣ]', 'P', origText)
        origText = re.sub('[ɋ]', 'q', origText)
        origText = re.sub('[Ɋ]', 'Q', origText)
        origText = re.sub('[ŕřŗṙṛṝȑȓṟɍɽ]', 'r', origText)
        origText = re.sub('[ŔŘŖṘṚṜȐȒṞɌⱤ]', 'R', origText)
        origText = re.sub('[śṥšṧşŝșṡṣṩ]', 's', origText)
        origText = re.sub('[ŚṤŠṦŞŜȘṠṢṨ]', 'S', origText)
        origText = re.sub('[ťţṱțẗⱦṫṭƭṯʈŧ]', 't', origText)
        origText = re.sub('[ŤŢṰȚȾṪṬƬṮƮŦ]', 'T', origText)
        origText = re.sub('[ʉúŭǔûṷüǘǚǜǖṳụűȕùủưứựừửữȗūṻųůũṹṵ]', 'u', origText)
        origText = re.sub('[ɄÚŬǓÛṶÜǗǙǛǕṲỤŰȔÙỦƯỨỰỪỬỮȖŪṺŲŮŨṸṴ]', 'U', origText)
        origText = re.sub('[ṿʋṽ]', 'v', origText)
        origText = re.sub('[ṾƲṼ]', 'V', origText)
        origText = re.sub('[ẃŵẅẇẉẁⱳẘ]', 'w', origText)
        origText = re.sub('[ẂŴẄẆẈẀⱲ]', 'W', origText)
        origText = re.sub('[ẍẋ]', 'x', origText)
        origText = re.sub('[ẌẊ]', 'X', origText)
        origText = re.sub('[ýŷÿẏỵỳƴỷȳẙɏỹ]', 'y', origText)
        origText = re.sub('[ÝŶŸẎỴỲƳỶȲɎỸ]', 'Y', origText)
        origText = re.sub('[ǽǣæ]', 'ae', origText)
        origText = re.sub('[ǼǢÆ]', 'AE', origText)
        origText = re.sub('[Þ]', 'th', origText)
        origText = re.sub('[þ]', 'TH', origText)
        origText = re.sub('[ß]', 'ss', origText)
        origText = re.sub('[ß]', 'SS', origText)
        origText = re.sub('[źžẑⱬżẓȥẕƶ]', 'z', origText)
        origText = re.sub('[ŹŽẐⱫŻẒȤẔƵ]', 'Z', origText)
        origText = re.sub('[œ]', 'oe', origText)
        origText = re.sub('[Œ]', 'OE', origText)
        origText = re.sub('[ð]', 'dj', origText)
        origText = re.sub('[Ð]', 'DJ', origText)
        origText = re.sub('[ĳ]', 'ij', origText)
        origText = re.sub('[Ĳ]', 'IJ', origText)
        origText = re.sub('[ǉ]', 'lj', origText)        
        origText = re.sub('[Ǉ]', 'LJ', origText)
        origText = re.sub('[ǌ]', 'nj', origText)
        origText = re.sub('[Ǌ]', 'NJ', origText)
        origText = re.sub('★','*',origText)
        return origText

    def get_only_numbers(origText):
        rgx = re.search("\d+", origText)
        origText = rgx.group()
        return str(origText)









