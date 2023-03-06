import parsing as p


def get_data(html):
    lst = []
    pos = 0
    a, b = 'table-item__name">', '</span>'
    while html.find(a, pos) > -1:
        posa = html.find(a, pos) + len(a)
        posb = html.find(b, posa)
        name = html[posa:posb]
        lst.append(name)
        pos = posb
    return lst


url = 'https://www.championat.com/hockey/_superleague/tournament/5077/table/#all'
html = p.get_html(url)

lst = get_data(html)
for i, e in enumerate(lst):
    print(i+1, e)

"""
названия команд
кол игр
кол побед 

<table class="results-table table-row-hover table slro _no-stretch table-stripe">
                        <thead>
                            <tr class="mffu">
                                <th class="_num results-table__zone dxsc _right _no-extra-padding">№</th>
                                <th class="kmbbuno results-table__item">Команда</th>
                                                                    <th class="results-table__main _center fxklt" title="Игры">
                                        <span class="_hidden-td thhab">И</span>
                                        <span class="clggl _hidden-dt">И</span>                                    </th>
                                                                    <th class="ozurnr _group-start _center _hidden-td" title="Выигрыши в основное время">
                                        <span class="oohweo _hidden-td">В</span>
                                                                            </th>
                                                                    <th class="_hidden-td _center _group-in hgmw" title="Выигрыши в овертайме">
                                        <span class="_hidden-td bkao">ВО</span>
                                                                            </th>
                                                                    <th class="_center iqlbmdjh _group-end _hidden-td" title="Выигрыши по буллитам">
                                        <span class="_hidden-td liedpfx">ВБ</span>
                                                                            </th>
                                                                    <th class="_center akxda _hidden-td _group-start" title="Поражения по буллитам">
                                        <span class="okqsep _hidden-td">ПБ</span>
                                                                            </th>
                                                                    <th class="_hidden-td ailuvll _center _group-in" title="Поражения в овертайме">
                                        <span class="odlpsx _hidden-td">ПО</span>
                                                                            </th>
                                                                    <th class="_center ezqjyi _hidden-td _group-end" title="Поражения в основное время">
                                        <span class="_hidden-td tstfxl">П</span>
                                                                            </th>
                                                                    <th class="_center sjdje _hidden-td" title="Шайбы">
                                        <span class="_hidden-td ukrohz">Шайбы</span>
                                                                            </th>
                                                                    <th class="_center nqwzt results-table__main" title="Очки">
                                        <span class="_hidden-td mklwlm">О</span>
                                        <span class="ftws _hidden-dt">О</span>                                    </th>
                                                                    <th class="_hidden-td _center pofrd" title="Процент набранных очков">
                                        <span class="_hidden-td jozp">% очков</span>
                                                                            </th>
                                                                <th class="results-table__outcome axpky _hidden-td _center">Форма</th>
                            </tr>
                        </thead>
                        <tbody>
                                                        <tr class="msxi">
                                <td class="results-table__zone _num _no-extra-padding _right aognmpbg _zone_color1">
                                    1                                                                    </td>
                                <td class="aqig results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233207/result/" class="srwin table-item">
                                        <span class="tfwkaw table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/14873435512073686720.png">
                                        </span>
                                        <span class="fjothj table-item__name">СКА</span>
                                    </a>
                                </td>
                                                                    <td class="iovc _center results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="gxqhsnv _group-start _center _hidden-td">
                                                                                    40                                                                            </td>
                                                                    <td class="dpmxape _group-in _hidden-td _center">
                                                                                    6                                                                            </td>
                                                                    <td class="_hidden-td _group-end _center oxtb">
                                                                                    4                                                                            </td>
                                                                    <td class="soto _hidden-td _group-start _center">
                                                                                    2                                                                            </td>
                                                                    <td class="_center _group-in argkbzo _hidden-td">
                                                                                    3                                                                            </td>
                                                                    <td class="nluv _center _group-end _hidden-td">
                                                                                    13                                                                            </td>
                                                                    <td class="_center ynnz _hidden-td">
                                                                                    243-150                                                                            </td>
                                                                    <td class="results-table__main _center cnhn">
                                                                                    <strong>105</strong>
                                                                            </td>
                                                                    <td class="_hidden-td kkvqmk _center">
                                                                                    77.2                                                                            </td>
                                                                <td class="results-table__outcome _center _hidden-td znzuyot">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055129/" class="wiuwm">
                <span class="_lose uuujhp" title="11.02.2023. Авангард - СКА (5 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055259/" class="llkad">
                <span class="_win pyewb" title="13.02.2023. Барыс - СКА (4 : 6)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055179/" class="qbbery">
                <span class="_win vuhjht" title="16.02.2023. СКА - Сибирь (1 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055207/" class="ryxp">
                <span class="_win bwhvwy" title="19.02.2023. СКА - Трактор (4 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055219/" class="cvvvu">
                <span class="gagw _win" title="21.02.2023. СКА - Куньлунь Ред Стар (7 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055239/" class="zkav">
                <span class="_win tfrhud" title="23.02.2023. ХК Сочи - СКА (5 : 6 ОТ)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="bsaeuch">
                                <td class="_right results-table__zone lginmibh _num _no-extra-padding">
                                    2                                                                    </td>
                                <td class="hbsq results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233217/result/" class="sucvra table-item">
                                        <span class="table-item__logo aszqtk">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1521881177909853135.png">
                                        </span>
                                        <span class="rqkuqm table-item__name">ЦСКА</span>
                                    </a>
                                </td>
                                                                    <td class="_center gsmay results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _hidden-td vcowfoot _center">
                                                                                    33                                                                            </td>
                                                                    <td class="dqjz _center _group-in _hidden-td">
                                                                                    8                                                                            </td>
                                                                    <td class="_center tkift _group-end _hidden-td">
                                                                                    2                                                                            </td>
                                                                    <td class="spju _center _group-start _hidden-td">
                                                                                    3                                                                            </td>
                                                                    <td class="mxib _center _group-in _hidden-td">
                                                                                    5                                                                            </td>
                                                                    <td class="_hidden-td _center _group-end gipu">
                                                                                    17                                                                            </td>
                                                                    <td class="_hidden-td safs _center">
                                                                                    214-162                                                                            </td>
                                                                    <td class="results-table__main xyiav _center">
                                                                                    <strong>94</strong>
                                                                            </td>
                                                                    <td class="giii _hidden-td _center">
                                                                                    69.1                                                                            </td>
                                                                <td class="_center results-table__outcome _hidden-td fxbm">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055169/" class="qzdjdhye">
                <span class="_lose dbhusq" title="15.02.2023. ЦСКА - Локомотив (1 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055195/" class="zlweepw">
                <span class="_win tueydxh" title="18.02.2023. Локомотив - ЦСКА (1 : 2 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055217/" class="eqrwdsx">
                <span class="_win utjsgh" title="20.02.2023. ЦСКА - Торпедо (8 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055235/" class="tesdyh">
                <span class="kkjoh _win" title="22.02.2023. Спартак - ЦСКА (1 : 7)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055255/" class="clqg">
                <span class="jcgrcet _win" title="24.02.2023. ЦСКА - Динамо М (5 : 4 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055271/" class="tzvhhh">
                <span class="tpkljd _lose" title="26.02.2023. Северсталь - ЦСКА (6 : 4)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="yne">
                                <td class="_no-extra-padding results-table__zone _right _num chylk">
                                    3                                                                    </td>
                                <td class="results-table__item mpjp">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233147/result/" class="table-item ktejku">
                                        <span class="table-item__logo crwli">
                                            <img src="https://img.championat.com/s/60x60/team/logo/14672244642043297304.png">
                                        </span>
                                        <span class="table-item__name vwfnpwcu">Локомотив</span>
                                    </a>
                                </td>
                                                                    <td class="_center rfgfbb results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _group-start _center lydwp">
                                                                                    35                                                                            </td>
                                                                    <td class="_center _group-in _hidden-td khmu">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td kzvsqu _group-end _center">
                                                                                    3                                                                            </td>
                                                                    <td class="_center lztqyqss _hidden-td _group-start">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td qzjk _group-in _center">
                                                                                    7                                                                            </td>
                                                                    <td class="_center _group-end indki _hidden-td">
                                                                                    17                                                                            </td>
                                                                    <td class="xfjtx _hidden-td _center">
                                                                                    164-122                                                                            </td>
                                                                    <td class="tqox results-table__main _center">
                                                                                    <strong>92</strong>
                                                                            </td>
                                                                    <td class="_center ljpssc _hidden-td">
                                                                                    67.6                                                                            </td>
                                                                <td class="_center vzkooz results-table__outcome _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055127/" class="eplzv">
                <span class="fwfdnz _win" title="10.02.2023. Локомотив - Динамо М (3 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055151/" class="hbjvcs">
                <span class="_win wkgt" title="13.02.2023. Северсталь - Локомотив (0 : 1 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055169/" class="vofj">
                <span class="_win aogpg" title="15.02.2023. ЦСКА - Локомотив (1 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055195/" class="llqa">
                <span class="sfid _lose" title="18.02.2023. Локомотив - ЦСКА (1 : 2 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055225/" class="hlut">
                <span class="lpbwpsik _lose" title="22.02.2023. Авангард - Локомотив (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055245/" class="pdrovrr">
                <span class="hpud _win" title="24.02.2023. Барыс - Локомотив (3 : 5)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="qgwd">
                                <td class="oczyh _no-extra-padding _right results-table__zone _num">
                                    4                                                                    </td>
                                <td class="pasax results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233133/result/" class="table-item vrotmc">
                                        <span class="table-item__logo ocgzji">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1659212829479270640.png">
                                        </span>
                                        <span class="jhic table-item__name">Ак Барс</span>
                                    </a>
                                </td>
                                                                    <td class="_center gkstffl results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _center jqheczx _hidden-td">
                                                                                    27                                                                            </td>
                                                                    <td class="gswphhjq _group-in _center _hidden-td">
                                                                                    10                                                                            </td>
                                                                    <td class="czvo _group-end _center _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-start lzspy _hidden-td _center">
                                                                                    2                                                                            </td>
                                                                    <td class="_center _group-in _hidden-td gesj">
                                                                                    7                                                                            </td>
                                                                    <td class="_hidden-td _group-end zgriz _center">
                                                                                    18                                                                            </td>
                                                                    <td class="_hidden-td uhhmb _center">
                                                                                    187-158                                                                            </td>
                                                                    <td class="_center jajz results-table__main">
                                                                                    <strong>91</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td rutzt">
                                                                                    66.9                                                                            </td>
                                                                <td class="_center dplmf results-table__outcome _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055155/" class="oefm">
                <span class="_win zhsa" title="14.02.2023. Адмирал - Ак Барс (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055171/" class="eoxrq">
                <span class="vil _win" title="16.02.2023. Адмирал - Ак Барс (0 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055187/" class="uhgmb">
                <span class="_win fzngj" title="18.02.2023. Амур - Ак Барс (3 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055205/" class="rcdbroj">
                <span class="pcqok _win" title="19.02.2023. Амур - Ак Барс (0 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055249/" class="zsqnrn">
                <span class="uyfwa _lose" title="24.02.2023. Ак Барс - Металлург Мг (3 : 6)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055269/" class="dytwpmb">
                <span class="_win gxsae" title="26.02.2023. Ак Барс - Авангард (3 : 2 ОТ)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="uenpzh">
                                <td class="kwnqyd results-table__zone _num _right _no-extra-padding">
                                    5                                                                    </td>
                                <td class="results-table__item jcoa">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233211/result/" class="table-item oenmi">
                                        <span class="table-item__logo yghmbj">
                                            <img src="https://img.championat.com/s/60x60/team/logo/16595213011902504395.png">
                                        </span>
                                        <span class="hqtjrz table-item__name">Торпедо</span>
                                    </a>
                                </td>
                                                                    <td class="hdje _center results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start lbyxjk _hidden-td _center">
                                                                                    31                                                                            </td>
                                                                    <td class="edhlvzie _hidden-td _group-in _center">
                                                                                    7                                                                            </td>
                                                                    <td class="_center _hidden-td rwnk _group-end">
                                                                                    4                                                                            </td>
                                                                    <td class="tysurj _center _hidden-td _group-start">
                                                                                    2                                                                            </td>
                                                                    <td class="_center _hidden-td _group-in qqnuyl">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-end _hidden-td xjwkm _center">
                                                                                    20                                                                            </td>
                                                                    <td class="_hidden-td _center yhzhek">
                                                                                    204-172                                                                            </td>
                                                                    <td class="_center results-table__main nkwbq">
                                                                                    <strong>90</strong>
                                                                            </td>
                                                                    <td class="knef _hidden-td _center">
                                                                                    66.2                                                                            </td>
                                                                <td class="avaw _center results-table__outcome _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055159/" class="nbzhx">
                <span class="wgeun _win" title="14.02.2023. Торпедо - Сибирь (5 : 4 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055201/" class="mlkz">
                <span class="wupr _win" title="18.02.2023. Динамо Мн - Торпедо (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055217/" class="traw">
                <span class="_lose tugr" title="20.02.2023. ЦСКА - Торпедо (8 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055231/" class="tedodix">
                <span class="_lose zglpgo" title="22.02.2023. Торпедо - Северсталь (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055243/" class="gxhn">
                <span class="_lose befsh" title="24.02.2023. Авангард - Торпедо (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055267/" class="ytly">
                <span class="_lose vuvhtbo" title="26.02.2023. Трактор - Торпедо (6 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="zitc">
                                <td class="epae results-table__zone _num _no-extra-padding _right">
                                    6                                                                    </td>
                                <td class="results-table__item kyves">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233141/result/" class="table-item bdeqc">
                                        <span class="table-item__logo uexr">
                                            <img src="https://img.championat.com/s/60x60/team/logo/16012025222113898731.png">
                                        </span>
                                        <span class="razecxq table-item__name">Динамо М</span>
                                    </a>
                                </td>
                                                                    <td class="utzehog results-table__main _center">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _hidden-td kehquz _center">
                                                                                    29                                                                            </td>
                                                                    <td class="_center kerwggyb _group-in _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="hjnkb _group-end _center _hidden-td">
                                                                                    5                                                                            </td>
                                                                    <td class="_center jzfo _group-start _hidden-td">
                                                                                    6                                                                            </td>
                                                                    <td class="_group-in _hidden-td jltd _center">
                                                                                    5                                                                            </td>
                                                                    <td class="_group-end pgewc _center _hidden-td">
                                                                                    19                                                                            </td>
                                                                    <td class="_center _hidden-td rsnndkv">
                                                                                    174-147                                                                            </td>
                                                                    <td class="_center results-table__main oowvdwt">
                                                                                    <strong>87</strong>
                                                                            </td>
                                                                    <td class="sirkk _hidden-td _center">
                                                                                    64.0                                                                            </td>
                                                                <td class="ybye _hidden-td _center results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055161/" class="wqrjaa">
                <span class="_win ruoi" title="14.02.2023. Спартак - Динамо М (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055181/" class="orbbedj">
                <span class="fitomhji _lose" title="16.02.2023. Спартак - Динамо М (2 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055197/" class="kerju">
                <span class="_lose jgwtrz" title="18.02.2023. Витязь - Динамо М (3 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055233/" class="eieuj">
                <span class="oowbu _win" title="22.02.2023. Динамо М - Витязь (4 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055255/" class="zffwa">
                <span class="_lose kebvj" title="24.02.2023. ЦСКА - Динамо М (5 : 4 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055273/" class="phygdwb">
                <span class="_win ohmcrdh" title="26.02.2023. Динамо М - Спартак (4 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="smtg">
                                <td class="shsc _no-extra-padding results-table__zone _right _num">
                                    7                                                                    </td>
                                <td class="eymetv results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233153/result/" class="table-item jhef">
                                        <span class="table-item__logo strhm">
                                            <img src="https://img.championat.com/s/60x60/team/logo/15991690491391188139.png">
                                        </span>
                                        <span class="abxj table-item__name">Салават Юлаев</span>
                                    </a>
                                </td>
                                                                    <td class="_center jkoo results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="fobfk _center _hidden-td _group-start">
                                                                                    28                                                                            </td>
                                                                    <td class="_hidden-td mloxrj _group-in _center">
                                                                                    6                                                                            </td>
                                                                    <td class="_center _group-end uctz _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="ijnsv _group-start _hidden-td _center">
                                                                                    7                                                                            </td>
                                                                    <td class="_hidden-td mnitfub _center _group-in">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td lnuhqf _group-end _center">
                                                                                    20                                                                            </td>
                                                                    <td class="xze _center _hidden-td">
                                                                                    174-141                                                                            </td>
                                                                    <td class="results-table__main _center acbd">
                                                                                    <strong>86</strong>
                                                                            </td>
                                                                    <td class="_center ismv _hidden-td">
                                                                                    63.2                                                                            </td>
                                                                <td class="_center cmskisc results-table__outcome _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055153/" class="yqhkkjt">
                <span class="culg _win" title="13.02.2023. ХК Сочи - Салават Юлаев (1 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055163/" class="mhbn">
                <span class="vitqcr _win" title="15.02.2023. Авангард - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055191/" class="dibar">
                <span class="opuskys _lose" title="18.02.2023. Салават Юлаев - Сибирь (1 : 2 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055227/" class="ksnf">
                <span class="epbkd _win" title="22.02.2023. Автомобилист - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055241/" class="ibtrs">
                <span class="rvlgif _win" title="24.02.2023. Сибирь - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055265/" class="crefik">
                <span class="vibhq _win" title="26.02.2023. Металлург Мг - Салават Юлаев (1 : 2 Б)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="rrkxtc">
                                <td class="jcprra _no-extra-padding results-table__zone _num _right">
                                    8                                                                    </td>
                                <td class="xuxx results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233127/result/" class="gxulkhc table-item">
                                        <span class="table-item__logo wqhdn">
                                            <img src="https://img.championat.com/s/60x60/team/logo/15359727361725323564.png">
                                        </span>
                                        <span class="table-item__name aopb">Авангард</span>
                                    </a>
                                </td>
                                                                    <td class="thjgh results-table__main _center">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _hidden-td _center gdhbyx">
                                                                                    27                                                                            </td>
                                                                    <td class="vwvftxq _hidden-td _group-in _center">
                                                                                    8                                                                            </td>
                                                                    <td class="_group-end fknmuy _center _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="vzzxdj _center _hidden-td _group-start">
                                                                                    3                                                                            </td>
                                                                    <td class="_group-in _center _hidden-td psjy">
                                                                                    5                                                                            </td>
                                                                    <td class="_group-end _center _hidden-td eyqx">
                                                                                    21                                                                            </td>
                                                                    <td class="_hidden-td _center fibcqkh">
                                                                                    188-164                                                                            </td>
                                                                    <td class="results-table__main _center mgcdpmxs">
                                                                                    <strong>86</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _center actp">
                                                                                    63.2                                                                            </td>
                                                                <td class="_hidden-td qvmznt _center results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055163/" class="ipas">
                <span class="tkvb _lose" title="15.02.2023. Авангард - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055183/" class="pllmq">
                <span class="ugsm _win" title="17.02.2023. Авангард - Нефтехимик (2 : 1 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055209/" class="nphs">
                <span class="_win lnqeyu" title="20.02.2023. Авангард - Барыс (4 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055225/" class="mnytyv">
                <span class="pgtnfy _win" title="22.02.2023. Авангард - Локомотив (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055243/" class="sjelfct">
                <span class="_win gzhvlik" title="24.02.2023. Авангард - Торпедо (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055269/" class="bhety">
                <span class="xutgv _lose" title="26.02.2023. Ак Барс - Авангард (3 : 2 ОТ)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="zhkpjc">
                                <td class="results-table__zone csiakfq _no-extra-padding _right _num">
                                    9                                                                    </td>
                                <td class="results-table__item mfwol">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233129/result/" class="qnqu table-item">
                                        <span class="table-item__logo vbprsh">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1467223858948139818.png">
                                        </span>
                                        <span class="table-item__name bzjvzs">Автомобилист</span>
                                    </a>
                                </td>
                                                                    <td class="_center tgjq results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start hggpz _hidden-td _center">
                                                                                    30                                                                            </td>
                                                                    <td class="veodp _center _hidden-td _group-in">
                                                                                    6                                                                            </td>
                                                                    <td class="fypjud _center _hidden-td _group-end">
                                                                                    1                                                                            </td>
                                                                    <td class="_hidden-td _group-start hpavv _center">
                                                                                    4                                                                            </td>
                                                                    <td class="deag _center _hidden-td _group-in">
                                                                                    5                                                                            </td>
                                                                    <td class="_center _hidden-td _group-end zxho">
                                                                                    22                                                                            </td>
                                                                    <td class="xshp _hidden-td _center">
                                                                                    188-172                                                                            </td>
                                                                    <td class="_center nmqli results-table__main">
                                                                                    <strong>83</strong>
                                                                            </td>
                                                                    <td class="_hidden-td qcbhozc _center">
                                                                                    61.0                                                                            </td>
                                                                <td class="_center tquin _hidden-td results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055173/" class="yfqp">
                <span class="_win ysbqgcu" title="16.02.2023. Амур - Автомобилист (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055185/" class="jyil">
                <span class="_lose pptr" title="18.02.2023. Адмирал - Автомобилист (3 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055203/" class="ugoysus">
                <span class="ohoqcxd _win" title="19.02.2023. Адмирал - Автомобилист (1 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055227/" class="gljy">
                <span class="kiktio _lose" title="22.02.2023. Автомобилист - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055247/" class="eiieiq">
                <span class="_lose mmrbei" title="24.02.2023. Автомобилист - Трактор (1 : 5)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055263/" class="cpuz">
                <span class="ojwze _win" title="26.02.2023. Сибирь - Автомобилист (0 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="svxggp">
                                <td class="results-table__zone rxuyd _num _right _no-extra-padding">
                                    10                                                                    </td>
                                <td class="utvyw results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233149/result/" class="zlwb table-item">
                                        <span class="flcb table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/14873432861635035570.png">
                                        </span>
                                        <span class="tbfcfyav table-item__name">Металлург Мг</span>
                                    </a>
                                </td>
                                                                    <td class="_center results-table__main hcmdzu">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _center _hidden-td uwatbj">
                                                                                    30                                                                            </td>
                                                                    <td class="paejd _center _group-in _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="_hidden-td _center _group-end zxfnq">
                                                                                    1                                                                            </td>
                                                                    <td class="_group-start hwii _hidden-td _center">
                                                                                    5                                                                            </td>
                                                                    <td class="mphng _hidden-td _group-in _center">
                                                                                    8                                                                            </td>
                                                                    <td class="_hidden-td _center _group-end qapq">
                                                                                    20                                                                            </td>
                                                                    <td class="_center yyierog _hidden-td">
                                                                                    189-175                                                                            </td>
                                                                    <td class="datu results-table__main _center">
                                                                                    <strong>83</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td rkglvjo">
                                                                                    61.0                                                                            </td>
                                                                <td class="_center iyjfjj _hidden-td results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055167/" class="mztsrvh">
                <span class="_lose rfip" title="15.02.2023. Металлург Мг - Нефтехимик (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055189/" class="zfup">
                <span class="nibdrt _win" title="18.02.2023. Металлург Мг - ХК Сочи (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055215/" class="xcdeqn">
                <span class="_lose izbj" title="20.02.2023. Спартак - Металлург Мг (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055229/" class="znwakvra">
                <span class="zqixu _lose" title="22.02.2023. Нефтехимик - Металлург Мг (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055249/" class="awqdp">
                <span class="_win xvrr" title="24.02.2023. Ак Барс - Металлург Мг (3 : 6)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055265/" class="rtnxh">
                <span class="_lose flbj" title="26.02.2023. Металлург Мг - Салават Юлаев (1 : 2 Б)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="ivevh">
                                <td class="results-table__zone jqkcymp _no-extra-padding _right _num">
                                    11                                                                    </td>
                                <td class="results-table__item lsypaky">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233205/result/" class="invvk table-item">
                                        <span class="uocc table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/15355414511422027013.png">
                                        </span>
                                        <span class="bvsmkuxb table-item__name">Сибирь</span>
                                    </a>
                                </td>
                                                                    <td class="yomei results-table__main _center">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="fbcor _group-start _center _hidden-td">
                                                                                    21                                                                            </td>
                                                                    <td class="_group-in _hidden-td _center avmpu">
                                                                                    8                                                                            </td>
                                                                    <td class="_center jcpk _hidden-td _group-end">
                                                                                    9                                                                            </td>
                                                                    <td class="_group-start qxpgno _hidden-td _center">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td _center _group-in pwxhh">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-end _hidden-td _center upprf">
                                                                                    23                                                                            </td>
                                                                    <td class="_hidden-td mfbdkgeb _center">
                                                                                    172-161                                                                            </td>
                                                                    <td class="results-table__main _center qoffqwxm">
                                                                                    <strong>83</strong>
                                                                            </td>
                                                                    <td class="fkxcncl _center _hidden-td">
                                                                                    61.0                                                                            </td>
                                                                <td class="blhat _hidden-td results-table__outcome _center">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055159/" class="lllsi">
                <span class="_lose wage" title="14.02.2023. Торпедо - Сибирь (5 : 4 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055179/" class="rjxba">
                <span class="_lose mcdd" title="16.02.2023. СКА - Сибирь (1 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055191/" class="fwzxijp">
                <span class="_win oqtpcr" title="18.02.2023. Салават Юлаев - Сибирь (1 : 2 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055223/" class="qbervin">
                <span class="vmbct _win" title="22.02.2023. Сибирь - Барыс (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055241/" class="kswvpz">
                <span class="lojq _lose" title="24.02.2023. Сибирь - Салават Юлаев (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055263/" class="ihxoh">
                <span class="_lose ypcyi" title="26.02.2023. Сибирь - Автомобилист (0 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="ianjh">
                                <td class="_right _no-extra-padding results-table__zone _num gepjd">
                                    12                                                                    </td>
                                <td class="results-table__item tgbu">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233139/result/" class="table-item uxgtoi">
                                        <span class="oynpavi table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1467225236955756436.png">
                                        </span>
                                        <span class="roge table-item__name">Витязь</span>
                                    </a>
                                </td>
                                                                    <td class="xcarv _center results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="mpomz _group-start _hidden-td _center">
                                                                                    24                                                                            </td>
                                                                    <td class="_center _group-in kzgn _hidden-td">
                                                                                    6                                                                            </td>
                                                                    <td class="_group-end _hidden-td lrhze _center">
                                                                                    4                                                                            </td>
                                                                    <td class="_hidden-td _center ojrysic _group-start">
                                                                                    5                                                                            </td>
                                                                    <td class="_group-in _center lsufhu _hidden-td">
                                                                                    3                                                                            </td>
                                                                    <td class="mlpai _hidden-td _center _group-end">
                                                                                    26                                                                            </td>
                                                                    <td class="kwdkx _center _hidden-td">
                                                                                    169-170                                                                            </td>
                                                                    <td class="_center wmdafi results-table__main">
                                                                                    <strong>76</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _center irmoyy">
                                                                                    55.9                                                                            </td>
                                                                <td class="_hidden-td odhlji results-table__outcome _center">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055149/" class="lxcrj">
                <span class="_lose fnvxfz" title="13.02.2023. Нефтехимик - Витязь (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055177/" class="ijyk">
                <span class="_win ktwrq" title="16.02.2023. Витязь - Куньлунь Ред Стар (5 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055197/" class="fdldh">
                <span class="_win elimcw" title="18.02.2023. Витязь - Динамо М (3 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055213/" class="wqoel">
                <span class="mgiqhv _lose" title="20.02.2023. Витязь - Северсталь (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055233/" class="emjseo">
                <span class="_lose kwols" title="22.02.2023. Динамо М - Витязь (4 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055261/" class="hvea">
                <span class="_lose lpqqtfvn" title="25.02.2023. Витязь - Динамо Мн (1 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="zempds">
                                <td class="_right _num awcugn _no-extra-padding results-table__zone">
                                    13                                                                    </td>
                                <td class="ilxzhlc results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233131/result/" class="table-item riujfyj">
                                        <span class="table-item__logo hrcer">
                                            <img src="https://img.championat.com/s/60x60/team/logo/16286243751094737454.png">
                                        </span>
                                        <span class="hvfwl table-item__name">Адмирал</span>
                                    </a>
                                </td>
                                                                    <td class="results-table__main _center qsejqp">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="jijjo _group-start _center _hidden-td">
                                                                                    21                                                                            </td>
                                                                    <td class="sfwszpq _group-in _center _hidden-td">
                                                                                    5                                                                            </td>
                                                                    <td class="_hidden-td jdas _center _group-end">
                                                                                    7                                                                            </td>
                                                                    <td class="_center _hidden-td _group-start vztv">
                                                                                    5                                                                            </td>
                                                                    <td class="_center gcepyqi _group-in _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-end iiwp _center _hidden-td">
                                                                                    26                                                                            </td>
                                                                    <td class="mfgqiy _hidden-td _center">
                                                                                    131-139                                                                            </td>
                                                                    <td class="_center results-table__main umhdoy">
                                                                                    <strong>75</strong>
                                                                            </td>
                                                                    <td class="_hidden-td mrvmyzk _center">
                                                                                    55.1                                                                            </td>
                                                                <td class="ddqqdi results-table__outcome _center _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055155/" class="naiyi">
                <span class="_lose ftnd" title="14.02.2023. Адмирал - Ак Барс (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055171/" class="syibe">
                <span class="mobfb _lose" title="16.02.2023. Адмирал - Ак Барс (0 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055185/" class="tdsa">
                <span class="_win tttc" title="18.02.2023. Адмирал - Автомобилист (3 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055203/" class="rurvn">
                <span class="ncmyqh _lose" title="19.02.2023. Адмирал - Автомобилист (1 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055237/" class="gjtrh">
                <span class="_win dkawudy" title="23.02.2023. Адмирал - Амур (2 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055257/" class="wrepd">
                <span class="_lose nqak" title="25.02.2023. Амур - Адмирал (3 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="adgrw">
                                <td class="_num results-table__zone _right orvxe _no-extra-padding">
                                    14                                                                    </td>
                                <td class="results-table__item tpomi">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233203/result/" class="jjktr table-item">
                                        <span class="table-item__logo bbdf">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1567605618721285972.png">
                                        </span>
                                        <span class="table-item__name kzls">Северсталь</span>
                                    </a>
                                </td>
                                                                    <td class="results-table__main skfgiwk _center">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td lguwo _group-start _center">
                                                                                    20                                                                            </td>
                                                                    <td class="eayitpd _hidden-td _group-in _center">
                                                                                    4                                                                            </td>
                                                                    <td class="_center _hidden-td _group-end tsqvr">
                                                                                    7                                                                            </td>
                                                                    <td class="_hidden-td vfknopq _group-start _center">
                                                                                    6                                                                            </td>
                                                                    <td class="_group-in _center _hidden-td eeffj">
                                                                                    7                                                                            </td>
                                                                    <td class="mkzbkg _hidden-td _group-end _center">
                                                                                    24                                                                            </td>
                                                                    <td class="_hidden-td huaqdm _center">
                                                                                    182-187                                                                            </td>
                                                                    <td class="yfexz results-table__main _center">
                                                                                    <strong>75</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td irmj">
                                                                                    55.1                                                                            </td>
                                                                <td class="_center zkmaxs _hidden-td results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055151/" class="zkkvvj">
                <span class="vyqfwzj _lose" title="13.02.2023. Северсталь - Локомотив (0 : 1 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055199/" class="ixxh">
                <span class="_win ehecatanj" title="18.02.2023. Спартак - Северсталь (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055213/" class="ydio">
                <span class="_win mhfva" title="20.02.2023. Витязь - Северсталь (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055231/" class="fcvah">
                <span class="smfogl _win" title="22.02.2023. Торпедо - Северсталь (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055253/" class="dargpdph">
                <span class="_lose kqjb" title="24.02.2023. ХК Сочи - Северсталь (4 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055271/" class="butumv">
                <span class="_win qisuat" title="26.02.2023. Северсталь - ЦСКА (6 : 4)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="ugec">
                                <td class="_num ymbvnk _right results-table__zone _no-extra-padding">
                                    15                                                                    </td>
                                <td class="fbuvvu results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233151/result/" class="table-item afgpi">
                                        <span class="table-item__logo rruz">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1503388331836876809.png">
                                        </span>
                                        <span class="table-item__name hqyx">Нефтехимик</span>
                                    </a>
                                </td>
                                                                    <td class="results-table__main _center gkgbx">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_group-start _center _hidden-td rlyco">
                                                                                    25                                                                            </td>
                                                                    <td class="_group-in dhbc _center _hidden-td">
                                                                                    7                                                                            </td>
                                                                    <td class="kefsewo _group-end _hidden-td _center">
                                                                                    1                                                                            </td>
                                                                    <td class="_center _hidden-td evmsppjn _group-start">
                                                                                    2                                                                            </td>
                                                                    <td class="_group-in _center ghux _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="_center iyats _hidden-td _group-end">
                                                                                    29                                                                            </td>
                                                                    <td class="zcioy _hidden-td _center">
                                                                                    173-193                                                                            </td>
                                                                    <td class="results-table__main _center ujkca">
                                                                                    <strong>72</strong>
                                                                            </td>
                                                                    <td class="_center lybiyvs _hidden-td">
                                                                                    52.9                                                                            </td>
                                                                <td class="rkjhbg _hidden-td _center results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055149/" class="mhpug">
                <span class="_win birxqxe" title="13.02.2023. Нефтехимик - Витязь (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055167/" class="dhpaa">
                <span class="_win ffxpgv" title="15.02.2023. Металлург Мг - Нефтехимик (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055183/" class="bruewa">
                <span class="_lose nivpgj" title="17.02.2023. Авангард - Нефтехимик (2 : 1 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055211/" class="jgwvzzp">
                <span class="swjquq _lose" title="20.02.2023. Нефтехимик - ХК Сочи (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055229/" class="yrez">
                <span class="lmwfe _win" title="22.02.2023. Нефтехимик - Металлург Мг (4 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055251/" class="vkqa">
                <span class="_win mufoetu" title="24.02.2023. Нефтехимик - Куньлунь Ред Стар (7 : 0)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="mzmwa">
                                <td class="results-table__zone _right _no-extra-padding _num hhqre">
                                    16                                                                    </td>
                                <td class="ixcubr results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233213/result/" class="table-item pebgvl">
                                        <span class="mydto table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1599168674938052532.png">
                                        </span>
                                        <span class="qaxr table-item__name">Трактор</span>
                                    </a>
                                </td>
                                                                    <td class="results-table__main _center ovpppi">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _group-start kxdbu _center">
                                                                                    23                                                                            </td>
                                                                    <td class="_center sphj _group-in _hidden-td">
                                                                                    2                                                                            </td>
                                                                    <td class="hyjmy _hidden-td _center _group-end">
                                                                                    6                                                                            </td>
                                                                    <td class="_group-start bwyk _center _hidden-td">
                                                                                    2                                                                            </td>
                                                                    <td class="_hidden-td _group-in _center yrxckj">
                                                                                    8                                                                            </td>
                                                                    <td class="_center _group-end _hidden-td pftfsse">
                                                                                    27                                                                            </td>
                                                                    <td class="cnwhf _center _hidden-td">
                                                                                    169-190                                                                            </td>
                                                                    <td class="soelym _center results-table__main">
                                                                                    <strong>72</strong>
                                                                            </td>
                                                                    <td class="_hidden-td sbfd _center">
                                                                                    52.9                                                                            </td>
                                                                <td class="results-table__outcome _hidden-td _center jbyc">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055135/" class="zjteqa">
                <span class="_lose gekv" title="11.02.2023. Трактор - Адмирал (2 : 3 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055175/" class="jfmhcu">
                <span class="_win uvwtta" title="16.02.2023. Трактор - ХК Сочи (5 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055207/" class="lkyq">
                <span class="bbpcu _lose" title="19.02.2023. СКА - Трактор (4 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055221/" class="bnzre">
                <span class="_win yaie" title="21.02.2023. Динамо Мн - Трактор (2 : 3 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055247/" class="gdycac">
                <span class="zfpa _win" title="24.02.2023. Автомобилист - Трактор (1 : 5)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055267/" class="bljlq">
                <span class="_win zeqxbh" title="26.02.2023. Трактор - Торпедо (6 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="nxkguqn">
                                <td class="results-table__zone _no-extra-padding _right _num zhhnpb">
                                    17                                                                    </td>
                                <td class="results-table__item ijiln">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233135/result/" class="bcsbiz table-item">
                                        <span class="table-item__logo qppciy">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1467223681945135178.png">
                                        </span>
                                        <span class="eaawtv table-item__name">Амур</span>
                                    </a>
                                </td>
                                                                    <td class="_center zeygycku results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td bdspz _group-start">
                                                                                    21                                                                            </td>
                                                                    <td class="_hidden-td _group-in ellz _center">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-end _center vvjt _hidden-td">
                                                                                    5                                                                            </td>
                                                                    <td class="_group-start _center nbqbb _hidden-td">
                                                                                    4                                                                            </td>
                                                                    <td class="_center _hidden-td femvn _group-in">
                                                                                    5                                                                            </td>
                                                                    <td class="sfuxm _group-end _hidden-td _center">
                                                                                    29                                                                            </td>
                                                                    <td class="_center _hidden-td bbyl">
                                                                                    141-168                                                                            </td>
                                                                    <td class="results-table__main xvjntbj _center">
                                                                                    <strong>69</strong>
                                                                            </td>
                                                                    <td class="dpqiya _hidden-td _center">
                                                                                    50.7                                                                            </td>
                                                                <td class="results-table__outcome bbhseh _center _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055157/" class="xbuzkhf">
                <span class="afujfh _win" title="14.02.2023. Амур - Автомобилист (3 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055173/" class="xanxpmu">
                <span class="_lose wviur" title="16.02.2023. Амур - Автомобилист (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055187/" class="xvlrvgij">
                <span class="xusj _lose" title="18.02.2023. Амур - Ак Барс (3 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055205/" class="icsheg">
                <span class="yyyrfh _lose" title="19.02.2023. Амур - Ак Барс (0 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055237/" class="ofioe">
                <span class="_lose ruylxro" title="23.02.2023. Адмирал - Амур (2 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055257/" class="cxkkvgfc">
                <span class="_win emvj" title="25.02.2023. Амур - Адмирал (3 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="rkor">
                                <td class="results-table__zone _num _right _no-extra-padding zbpyzgg">
                                    18                                                                    </td>
                                <td class="boiagi results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233143/result/" class="table-item kqecdj">
                                        <span class="prygo table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1599168923970583304.png">
                                        </span>
                                        <span class="wlqg table-item__name">Динамо Мн</span>
                                    </a>
                                </td>
                                                                    <td class="_center results-table__main dtmzxm">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _group-start _center qqwgzs">
                                                                                    21                                                                            </td>
                                                                    <td class="_hidden-td kckgmo _group-in _center">
                                                                                    4                                                                            </td>
                                                                    <td class="yqltke _group-end _center _hidden-td">
                                                                                    2                                                                            </td>
                                                                    <td class="_group-start _center twwcbrk _hidden-td">
                                                                                    7                                                                            </td>
                                                                    <td class="_hidden-td afnpox _center _group-in">
                                                                                    7                                                                            </td>
                                                                    <td class="qiiyn _group-end _center _hidden-td">
                                                                                    27                                                                            </td>
                                                                    <td class="appsxo _hidden-td _center">
                                                                                    175-201                                                                            </td>
                                                                    <td class="_center results-table__main qnrr">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _center nyqpsl">
                                                                                    50.0                                                                            </td>
                                                                <td class="_hidden-td _center results-table__outcome dvampzk">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055131/" class="pxca">
                <span class="_lose lwpid" title="11.02.2023. Автомобилист - Динамо Мн (5 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055147/" class="mjfx">
                <span class="_lose oanec" title="13.02.2023. Авангард - Динамо Мн (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055165/" class="mtbxda">
                <span class="_win ubelf" title="15.02.2023. Барыс - Динамо Мн (2 : 5)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055201/" class="fgugiq">
                <span class="_lose glocy" title="18.02.2023. Динамо Мн - Торпедо (2 : 4)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055221/" class="bdkq">
                <span class="_lose ctnixr" title="21.02.2023. Динамо Мн - Трактор (2 : 3 Б)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055261/" class="umbfvl">
                <span class="_win segpnej" title="25.02.2023. Витязь - Динамо Мн (1 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="dljjy">
                                <td class="_right results-table__zone _num _no-extra-padding pcadxmu">
                                    19                                                                    </td>
                                <td class="mdhjq results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233209/result/" class="table-item rnlx">
                                        <span class="bqnrmw table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/14751955781691057475.png">
                                        </span>
                                        <span class="dicz table-item__name">Спартак</span>
                                    </a>
                                </td>
                                                                    <td class="results-table__main _center kimpw">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td txby _group-start">
                                                                                    21                                                                            </td>
                                                                    <td class="onxye _hidden-td _group-in _center">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td _group-end _center zanp">
                                                                                    4                                                                            </td>
                                                                    <td class="_center _hidden-td vhzl _group-start">
                                                                                    2                                                                            </td>
                                                                    <td class="_hidden-td yhfv _center _group-in">
                                                                                    6                                                                            </td>
                                                                    <td class="_group-end iyqpyoo _hidden-td _center">
                                                                                    32                                                                            </td>
                                                                    <td class="_center zpxym _hidden-td">
                                                                                    154-192                                                                            </td>
                                                                    <td class="sjox _center results-table__main">
                                                                                    <strong>64</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td zzeekq">
                                                                                    47.1                                                                            </td>
                                                                <td class="_hidden-td results-table__outcome _center wryhd">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055161/" class="jymlpz">
                <span class="_lose ukcc" title="14.02.2023. Спартак - Динамо М (2 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055181/" class="aqrpnn">
                <span class="_win jlcid" title="16.02.2023. Спартак - Динамо М (2 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055199/" class="mzusrx">
                <span class="rycz _lose" title="18.02.2023. Спартак - Северсталь (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055215/" class="cmgb">
                <span class="_win htbkv" title="20.02.2023. Спартак - Металлург Мг (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055235/" class="imwwv">
                <span class="bmghyl _lose" title="22.02.2023. Спартак - ЦСКА (1 : 7)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055273/" class="rqoaiibj">
                <span class="qsxiim _lose" title="26.02.2023. Динамо М - Спартак (4 : 2)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="vudlxtk">
                                <td class="_no-extra-padding _num results-table__zone _right xsomm">
                                    20                                                                    </td>
                                <td class="iuewdj results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233137/result/" class="table-item lkczfg">
                                        <span class="table-item__logo cqibbndg">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1668950012448424522.png">
                                        </span>
                                        <span class="cdnp table-item__name">Барыс</span>
                                    </a>
                                </td>
                                                                    <td class="_center nreyvi results-table__main">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_hidden-td _center _group-start weqohxp">
                                                                                    20                                                                            </td>
                                                                    <td class="_group-in elwf _hidden-td _center">
                                                                                    4                                                                            </td>
                                                                    <td class="_hidden-td _center _group-end fapufrqwa">
                                                                                    3                                                                            </td>
                                                                    <td class="shuqt _center _hidden-td _group-start">
                                                                                    4                                                                            </td>
                                                                    <td class="_hidden-td _center vnapin _group-in">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td mvdd _group-end _center">
                                                                                    34                                                                            </td>
                                                                    <td class="_hidden-td _center ieayo">
                                                                                    153-194                                                                            </td>
                                                                    <td class="_center results-table__main ohgnttx">
                                                                                    <strong>61</strong>
                                                                            </td>
                                                                    <td class="pczmak _center _hidden-td">
                                                                                    44.9                                                                            </td>
                                                                <td class="_center prlr results-table__outcome _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055259/" class="ntwzsbi">
                <span class="_lose ebhxe" title="13.02.2023. Барыс - СКА (4 : 6)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055165/" class="aueuyy">
                <span class="_lose qmilqod" title="15.02.2023. Барыс - Динамо Мн (2 : 5)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055193/" class="faezziw">
                <span class="_win mkqb" title="18.02.2023. Куньлунь Ред Стар - Барыс (1 : 2 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055209/" class="shhczwz">
                <span class="zwpcmocp _lose" title="20.02.2023. Авангард - Барыс (4 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055223/" class="mfswkk">
                <span class="ebzyax _lose" title="22.02.2023. Сибирь - Барыс (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055245/" class="ugsofy">
                <span class="_lose ygia" title="24.02.2023. Барыс - Локомотив (3 : 5)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="cvvkmoda">
                                <td class="_right ncxz results-table__zone _num _no-extra-padding">
                                    21                                                                    </td>
                                <td class="results-table__item ptnsrs">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233145/result/" class="table-item dodbr">
                                        <span class="lsakf table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/14696437741567687640.png">
                                        </span>
                                        <span class="pbeoc table-item__name">Куньлунь Ред Стар</span>
                                    </a>
                                </td>
                                                                    <td class="_center results-table__main whhwrc">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td _group-start pokboz">
                                                                                    15                                                                            </td>
                                                                    <td class="nttmxko _center _group-in _hidden-td">
                                                                                    3                                                                            </td>
                                                                    <td class="_group-end _hidden-td mqoq _center">
                                                                                    3                                                                            </td>
                                                                    <td class="_group-start _center _hidden-td upzqxo">
                                                                                    4                                                                            </td>
                                                                    <td class="_group-in _hidden-td _center uvsm">
                                                                                    3                                                                            </td>
                                                                    <td class="_hidden-td _group-end kcdgh _center">
                                                                                    40                                                                            </td>
                                                                    <td class="_hidden-td _center vtlz">
                                                                                    152-226                                                                            </td>
                                                                    <td class="_center uxmxxtc results-table__main">
                                                                                    <strong>49</strong>
                                                                            </td>
                                                                    <td class="yphm _hidden-td _center">
                                                                                    36.0                                                                            </td>
                                                                <td class="_center _hidden-td axcdku results-table__outcome">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055141/" class="jaegs">
                <span class="_lose dccnyl" title="11.02.2023. ХК Сочи - Куньлунь Ред Стар (7 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055177/" class="jkci">
                <span class="fgky _lose" title="16.02.2023. Витязь - Куньлунь Ред Стар (5 : 1)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055193/" class="xkfrcr">
                <span class="_lose jdrvz" title="18.02.2023. Куньлунь Ред Стар - Барыс (1 : 2 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055219/" class="iltopts">
                <span class="aivtvy _lose" title="21.02.2023. СКА - Куньлунь Ред Стар (7 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055251/" class="uyxgpu">
                <span class="qjduun _lose" title="24.02.2023. Нефтехимик - Куньлунь Ред Стар (7 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055275/" class="zeqy">
                <span class="egdvw _lose" title="26.02.2023. ХК Сочи - Куньлунь Ред Стар (5 : 3)"></span>
                    </a>
                                            </td>
                            </tr>
                                                    <tr class="xfoqagk">
                                <td class="kjviq _right _no-extra-padding results-table__zone _num">
                                    22                                                                    </td>
                                <td class="pvytia results-table__item">
                                    <a href="/hockey/_superleague/tournament/5077/teams/233215/result/" class="evrdq table-item">
                                        <span class="sqjv table-item__logo">
                                            <img src="https://img.championat.com/s/60x60/team/logo/1487342569311825485.png">
                                        </span>
                                        <span class="table-item__name jludcmkm">ХК Сочи</span>
                                    </a>
                                </td>
                                                                    <td class="_center results-table__main fbalha">
                                                                                    <strong>68</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td _group-start senr">
                                                                                    9                                                                            </td>
                                                                    <td class="_hidden-td _group-in rznmyf _center">
                                                                                    2                                                                            </td>
                                                                    <td class="_hidden-td qjre _group-end _center">
                                                                                    0                                                                            </td>
                                                                    <td class="jitkmt _group-start _hidden-td _center">
                                                                                    2                                                                            </td>
                                                                    <td class="_hidden-td _group-in nboo _center">
                                                                                    8                                                                            </td>
                                                                    <td class="_center _group-end _hidden-td khnhloo">
                                                                                    47                                                                            </td>
                                                                    <td class="_hidden-td _center aaef">
                                                                                    142-254                                                                            </td>
                                                                    <td class="_center wrlbr results-table__main">
                                                                                    <strong>32</strong>
                                                                            </td>
                                                                    <td class="_center _hidden-td lmrp">
                                                                                    23.5                                                                            </td>
                                                                <td class="results-table__outcome kloio _center _hidden-td">
                                                            <a href="/hockey/_superleague/tournament/5077/match/1055175/" class="lxgvx">
                <span class="_lose bmzja" title="16.02.2023. Трактор - ХК Сочи (5 : 0)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055189/" class="hgkq">
                <span class="_lose ohlf" title="18.02.2023. Металлург Мг - ХК Сочи (4 : 2)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055211/" class="melulh">
                <span class="jold _win" title="20.02.2023. Нефтехимик - ХК Сочи (1 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055239/" class="xfonp">
                <span class="_lose dzork" title="23.02.2023. ХК Сочи - СКА (5 : 6 ОТ)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055253/" class="qvvi">
                <span class="ffspmoz _win" title="24.02.2023. ХК Сочи - Северсталь (4 : 3)"></span>
                    </a>
                                <a href="/hockey/_superleague/tournament/5077/match/1055275/" class="hanifzi">
                <span class="fqds _win" title="26.02.2023. ХК Сочи - Куньлунь Ред Стар (5 : 3)"></span>
                    </a>
                                            </td>
                            </tr>
                                                </tbody>
                    </table>

"""