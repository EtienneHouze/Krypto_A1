import matplotlib.pyplot as plt
from operator import itemgetter
from collections import OrderedDict

CIPHER = "5EMQ5YFFOQ6QYCQJ5YJQ6QYCQ3ED1QCOQ01YHQ2H61D0QM5YJQYQJ56D3Q6IQJ51Q51YHJQE2QCYDQJEQB1YL1QOEKQ2HECQM5ECQ6Q5YL1QZ11DQ6DI1FYHYZB1QM5ECQ6QBEL1QIEQ01YHBOQYD0QO1JQJEQ211BQ5YFFOQ6QADEMQOEKQM6BBQ2EH36L1QC1Q5YL1QDEJQEJ51HQYJJY_5C1DJIQZ11DQIF1_6YBBOQYFFE6DJ10QZOQ2YJ1QJEQJEHC1DJQYQ51Y0QB6A1QC6D1QFEEHQB1EDEHYQYD0QO1JQ6QMYIQDEJQJEQZBYC1QMYIQ6JQCOQ2YKBJQJ5YJQM56BIJQJ51QF1_KB6YHQ_5YHCIQE2Q51HQI6IJ1HQY22EH010QC1QYDQY3H11YZB1Q1DJ1HJY6DC1DJQYQFYII6EDQ2EHQC1QMYIQ1D31D01H10Q6DQ51HQ211ZB1Q51YHJQYD0QO1JQYCQ6QM5EBBOQZBYC1B1IIQ060Q6QDEJQ1D_EKHY31Q51HQ1CEJ6EDIQ060Q6QDEJQ211BQ_5YHC10QYJQJ5EI1QJHKBOQ31DK6D1Q1NFH1II6EDIQE2QDYJKH1QM56_5QJ5EK35QZKJQB6JJB1QC6HJ52KBQ6DQH1YB6JOQIEQE2J1DQYCKI10QKIQ060Q6QDEJQQZKJQE5QM5YJQ6IQCYDQJ5YJQ51Q0YH1IQIEQJEQY__KI1Q56CI1B2QCOQ01YHQ2H61D0Q6QFHEC6I1QOEKQ6QM6BBQ6CFHEL1Q6QM6BBQDEQBED31HQYIQ5YIQ1L1HQZ11DQCOQ5YZ6JQ_EDJ6DK1QJEQHKC6DYJ1QEDQ1L1HOQF1JJOQL1NYJ6EDQM56_5Q2EHJKD1QCYOQ06IF1DI1Q6QM6BBQ1D7EOQJ51QFH1I1DJQYD0QJ51QFYIJQI5YBBQZ1Q2EHQC1QJ51QFYIJQDEQ0EKZJQOEKQYH1QH635JQCOQZ1IJQE2Q2H61D0IQJ51H1QMEKB0QZ1Q2YHQB1IIQIK221H6D3QYCED3IJQCYDA6D0Q62QC1DQQYD0Q3E0QADEMIQM5OQJ51OQYH1QIEQ2YI56ED10QQ060QDEJQ1CFBEOQJ516HQ6CY36DYJ6EDIQIEQYII60KEKIBOQ6DQH1_YBB6D3QJ51QC1CEHOQE2QFYIJQIEHHEMQ6DIJ1Y0QE2QZ1YH6D3QJ516HQFH1I1DJQBEJQM6J5Q1GKYD6C6JOQZ1QA6D0Q1DEK35QJEQ6D2EHCQCOQCEJ51HQJ5YJQ6QI5YBBQYJJ1D0QJEQ51HQZKI6D1IIQJEQJ51QZ1IJQE2QCOQYZ6B6JOQYD0QI5YBBQ36L1Q51HQJ51Q1YHB61IJQ6D2EHCYJ6EDQYZEKJQ6JQ6Q5YL1QI11DQCOQYKDJQYD0Q26D0QJ5YJQI51Q6IQL1HOQ2YHQ2HECQZ16D3QJ51Q06IY3H11YZB1QF1HIEDQEKHQ2H61D0IQYBB131Q51HQJEQZ1QI51Q6IQYQB6L1BOQ_511H2KBQMECYDQM6J5QJ51QZ1IJQE2Q51YHJIQ6Q1NFBY6D10QJEQ51HQCOQCEJ51HIQMHED3IQM6J5QH13YH0QJEQJ5YJQFYHJQE2Q51HQFEHJ6EDQM56_5Q5YIQZ11DQM6J551B0Q2HECQ51HQI51QJEB0QC1QJ51QCEJ6L1IQYD0QH1YIEDIQE2Q51HQEMDQ_ED0K_JQYD0QJ51QJ1HCIQEDQM56_5QI51Q6IQM6BB6D3QJEQ36L1QKFQJ51QM5EB1QYD0QJEQ0EQCEH1QJ5YDQM1Q5YL1QYIA10Q6DQI5EHJQ6Q_YDDEJQMH6J1Q2KHJ51HQKFEDQJ56IQIKZ71_JQYJQFH1I1DJQEDBOQYIIKH1QCOQCEJ51HQJ5YJQYBBQM6BBQ3EQEDQM1BBQYD0Q6Q5YL1QY3Y6DQEZI1HL10QCOQ01YHQ2H61D0Q6DQJ56IQJH62B6D3QY22Y6HQJ5YJQC6IKD01HIJYD06D3IQYD0QD13B1_JQE__YI6EDQCEH1QC6I_5612Q6DQJ51QMEHB0QJ5YDQ1L1DQCYB6_1QYD0QM6_A10D1IIQYJQYBBQ1L1DJIQJ51QJMEQBYJJ1HQYH1QE2QB1IIQ2H1GK1DJQE__KHH1D_1QQ6DQEJ51HQH1IF1_JIQ6QYCQL1HOQM1BBQE22Q51H1QIEB6JK01Q6DQJ56IQJ1HH1IJH6YBQFYHY06I1Q6IQYQ31D6YBQZYBCQJEQCOQC6D0QYD0QJ51QOEKD3QIFH6D3Q_511HIQM6J5Q6JIQZEKDJ1EKIQFHEC6I1IQCOQE2J1DJ6C1IQC6I36L6D3Q51YHJQ1L1HOQJH11Q1L1HOQZKI5Q6IQ2KBBQE2Q2BEM1HIQYD0QED1QC635JQM6I5Q56CI1B2QJHYDI2EHC10Q6DJEQYQZKJJ1H2BOQJEQ2BEYJQYZEKJQ6DQJ56IQE_1YDQE2QF1H2KC1QYD0Q26D0Q56IQM5EB1Q1N6IJ1D_1Q6DQ6JQQJ51QJEMDQ6JI1B2Q6IQ06IY3H11YZB1QZKJQJ51DQYBBQYHEKD0QOEKQ26D0QYDQ6D1NFH1II6ZB1QZ1YKJOQE2QDYJKH1QJ56IQ6D0K_10QJ51QBYJ1Q_EKDJQCQJEQBYOQEKJQYQ3YH01DQEDQED1QE2QJ51QIBEF6D3Q56BBIQM56_5Q51H1Q6DJ1HI1_JQ1Y_5QEJ51HQM6J5QJ51QCEIJQ_5YHC6D3QLYH61JOQYD0Q2EHCQJ51QCEIJQBEL1BOQLYBB1OIQJ51Q3YH01DQ6IQI6CFB1QYD0Q6JQ6IQ1YIOQJEQF1H_16L1Q1L1DQKFEDQOEKHQ26HIJQ1DJHYD_1QJ5YJQJ51QFBYDQMYIQDEJQ01I63D10QZOQYQI_61DJ626_Q3YH01D1HQZKJQZOQYQCYDQM5EQM6I510QJEQ36L1Q56CI1B2QKFQ51H1QJEQJ51Q1D7EOC1DJQE2Q56IQEMDQI1DI6J6L1Q51YHJQCYDOQYQJ1YHQ5YL1Q6QYBH1Y0OQI510QJEQJ51QC1CEHOQE2Q6JIQ01FYHJ10QCYIJ1HQ6DQYQIKCC1HQ5EKI1QM56_5Q6IQDEMQH10K_10QJEQHK6DIQZKJQMYIQ56IQ2YLEKH6J1QH1IEHJQYD0QDEMQ6IQC6D1Q6QI5YBBQIEEDQZ1QCYIJ1HQE2QJ51QFBY_1QJ51Q3YH01D1HQ5YIQZ1_EC1QYJJY_510QJEQC1QM6J56DQJ51QBYIJQ21MQ0YOIQYD0Q51QM6BBQBEI1QDEJ56D3QJ51H1ZOQQCYOQSRQQYQMED01H2KBQI1H1D6JOQ5YIQJYA1DQFEII1II6EDQE2QCOQ1DJ6H1QIEKBQB6A1QJ51I1QIM11JQCEHD6D3IQE2QIFH6D3QM56_5Q6Q1D7EOQM6J5QCOQM5EB1Q51YHJQ6QYCQYBED1QYD0Q211BQJ51Q_5YHCQE2Q1N6IJ1D_1Q6DQJ56IQIFEJQM56_5QMYIQ_H1YJ10Q2EHQJ51QZB6IIQE2QIEKBIQB6A1QC6D1Q6QYCQIEQ5YFFOQCOQ01YHQ2H61D0QIEQYZIEHZ10Q6DQJ51Q1NGK6I6J1QI1DI1QE2QC1H1QJHYDGK6BQ1N6IJ1D_1QJ5YJQ6QD13B1_JQCOQJYB1DJIQ6QI5EKB0QZ1Q6D_YFYZB1QE2Q0HYM6D3QYQI6D3B1QIJHEA1QYJQJ51QFH1I1DJQCEC1DJQYD0QO1JQ6Q211BQJ5YJQ6QD1L1HQMYIQYQ3H1YJ1HQYHJ6IJQJ5YDQDEMQM51DQM56B1QJ51QBEL1BOQLYBB1OQJ11CIQM6J5QLYFEKHQYHEKD0QC1QYD0QJ51QC1H606YDQIKDQIJH6A1IQJ51QKFF1HQIKH2Y_1QE2QJ51Q6CF1D1JHYZB1Q2EB6Y31QE2QCOQJH11IQYD0QZKJQYQ21MQIJHYOQ3B1YCIQIJ1YBQ6DJEQJ51Q6DD1HQIYD_JKYHOQ6QJ5HEMQCOI1B2Q0EMDQYCED3QJ51QJYBBQ3HYIIQZOQJ51QJH6_AB6D3QIJH1YCQYD0QYIQ6QB61Q_BEI1QJEQJ51Q1YHJ5QYQJ5EKIYD0QKDADEMDQFBYDJIQYH1QDEJ6_10QZOQC1QM51DQ6Q51YHQJ51QZKPPQE2QJ51QB6JJB1QMEHB0QYCED3QJ51QIJYBAIQYD0Q3HEMQ2YC6B6YHQM6J5QJ51Q_EKDJB1IIQ6D01I_H6ZYZB1Q2EHCIQE2QJ51Q6DI1_JIQYD0Q2B61IQJ51DQ6Q211BQJ51QFH1I1D_1QE2QJ51QYBC635JOQM5EQ2EHC10QKIQ6DQ56IQEMDQ6CY31QYD0QJ51QZH1YJ5QE2QJ5YJQKD6L1HIYBQBEL1QM56_5QZ1YHIQYD0QIKIJY6DIQKIQYIQ6JQ2BEYJIQYHEKD0QKIQ6DQYDQ1J1HD6JOQE2QZB6IIQYD0QJ51DQCOQ2H61D0QM51DQ0YHAD1IIQEL1HIFH1Y0IQCOQ1O1IQYD0Q51YL1DQYD0Q1YHJ5QI11CQJEQ0M1BBQ6DQCOQIEKBQYD0QYZIEHZQ6JIQFEM1HQB6A1QJ51Q2EHCQE2QYQZ1BEL10QC6IJH1IIQJ51DQ6QE2J1DQJ56DAQM6J5QBED36D3QE5QMEKB0Q6Q_EKB0Q01I_H6Z1QJ51I1Q_ED_1FJ6EDIQ_EKB0Q6CFH1IIQKFEDQFYF1HQYBBQJ5YJQ6IQB6L6D3QIEQ2KBBQYD0QMYHCQM6J56DQC1QJ5YJQ6JQC635JQZ1QJ51QC6HHEHQE2QCOQIEKBQYIQCOQIEKBQ6IQJ51QC6HHEHQE2QJ51Q6D26D6J1Q3E0QEQCOQ2H61D0QQZKJQ6JQ6IQJEEQCK_5Q2EHQCOQIJH1D3J5QQ6QI6DAQKD01HQJ51QM1635JQE2QJ51QIFB1D0EKHQE2QJ51I1QL6I6EDIQQCYOQSTQQ6QADEMQDEJQM51J51HQIEC1Q01_16J2KBQIF6H6JIQ5YKDJQJ56IQIFEJQEHQM51J51HQ6JQZ1QJ51QMYHCQ_1B1IJ6YBQ2YD_OQ6DQCOQEMDQ51YHJQM56_5QCYA1IQ1L1HOJ56D3QYHEKD0QC1QI11CQB6A1QFYHY06I1Q6DQ2HEDJQE2QJ51Q5EKI1Q6IQYQ2EKDJY6DQQYQ2EKDJY6DQJEQM56_5Q6QYCQZEKD0QZOQYQ_5YHCQB6A1QC1BKI6DYQYD0Q51HQI6IJ1HIQ01I_1D06D3QYQ31DJB1QIBEF1QOEKQ_EC1QJEQYDQYH_5QM51H1QIEC1QJM1DJOQIJ1FIQBEM1HQ0EMDQMYJ1HQE2QJ51Q_B1YH1IJQ_HOIJYBQ3KI51IQ2HECQJ51QCYHZB1QHE_AQJ51QDYHHEMQMYBBQM56_5Q1D_BEI1IQ6JQYZEL1QJ51QJYBBQJH11IQM56_5Q1D_6H_B1QJ51QIFEJQYD0QJ51Q_EEBD1IIQE2QJ51QFBY_1Q6JI1B2QQ1L1HOJ56D3Q6CFYHJIQYQFB1YIYDJQZKJQIKZB6C1Q6CFH1II6EDQDEJQYQ0YOQFYII1IQEDQM56_5Q6Q0EQDEJQIF1D0QYDQ5EKHQJ51H1QJ51QOEKD3QCY601DIQ_EC1Q2HECQJ51QJEMDQJEQ21J_5QMYJ1HQQ6DDE_1DJQYD0QD1_1IIYHOQ1CFBEOC1DJQYD0Q2EHC1HBOQJ51QE__KFYJ6EDQE2QJ51Q0YK35J1HIQE2QA6D3IQYIQ6QJYA1QCOQH1IJQJ51H1QJ51Q601YQE2QJ51QEB0QFYJH6YH_5YBQB621Q6IQYMYA1D10QYHEKD0QC1Q6QI11QJ51CQEKHQEB0QYD_1IJEHIQ5EMQJ51OQ2EHC10QJ516HQ2H61D0I56FIQYD0Q_EDJHY_J10QYBB6YD_1IQYJQJ51Q2EKDJY6DQI601QYD0Q6Q211BQ5EMQ2EKDJY6DIQYD0QIJH1YCIQM1H1Q3KYH010QZOQZ1D126_1DJQIF6H6JIQ51QM5EQ6IQYQIJHYD31HQJEQJ51I1QI1DIYJ6EDIQ5YIQD1L1HQH1YBBOQ1D7EO10Q_EEBQH1FEI1QYJQJ51QI601QE2QYQ2EKDJY6DQY2J1HQJ51Q2YJ63K1QE2QYQM1YHOQIKCC1HQ0YOQQCYOQSUQQOEKQYIAQ62QOEKQI5YBBQI1D0QC1QZEEAIQCOQ01YHQ2H61D0Q6QZ1I11_5QOEKQ2EHQJ51QBEL1QE2Q3E0QH1B61L1QC1Q2HECQIK_5QYQOEA1Q6QD110QDEQCEH1QJEQZ1Q3K6010QY36JYJ10Q51YJ10QCOQ51YHJQ21HC1DJIQIK226_61DJBOQE2Q6JI1B2Q6QMYDJQIJHY6DIQJEQBKBBQC1QYD0Q6Q26D0QJ51CQJEQF1H21_J6EDQ6DQCOQ5EC1HQE2J1DQ0EQ6QIJH6L1QJEQYBBYOQJ51QZKHD6D3Q21L1HQE2QCOQZBEE0QYD0QOEKQ5YL1QD1L1HQM6JD1II10QYDOJ56D3QIEQKDIJ1Y0OQIEQKD_1HJY6DQYIQCOQ51YHJQZKJQD110Q6Q_ED21IIQJ56IQJEQOEKQCOQ01YHQ2H61D0QM5EQ5YL1QIEQE2J1DQ1D0KH10QJ51QYD3K6I5QE2QM6JD1II6D3QCOQIK001DQJHYDI6J6EDIQ2HECQIEHHEMQJEQ6CCE01HYJ1Q7EOQYD0Q2HECQIM11JQC1BYD_5EBOQJEQL6EB1DJQFYII6EDIQ6QJH1YJQCOQFEEHQ51YHJQB6A1QYQI6_AQ_56B0QYD0Q3HYJ62OQ6JIQ1L1HOQ2YD_OQ0EQDEJQC1DJ6EDQJ56IQY3Y6DQJ51H1QYH1QF1EFB1QM5EQMEKB0Q_1DIKH1QC1Q2EHQ6JQQCYOQSVQQJ51Q_ECCEDQF1EFB1QE2QJ51QFBY_1QADEMQC1QYBH1Y0OQYD0QBEL1QC1QFYHJ6_KBYHBOQJ51Q_56B0H1DQM51DQYJQ26HIJQ6QYIIE_6YJ10QM6J5QJ51CQYD0Q6DGK6H10Q6DQYQ2H61D0BOQJED1QYZEKJQJ516HQLYH6EKIQJH62B1IQIEC1Q2YD_610QJ5YJQ6QM6I510QJEQH606_KB1QJ51CQYD0QJKHD10Q2HECQC1Q6DQ1N_1106D3Q6BBQ5KCEKHQ6Q060QDEJQYBBEMQJ5YJQ_6H_KCIJYD_1QJEQ3H61L1QC1Q6QEDBOQ21BJQCEIJQA11DBOQM5YJQ6Q5YL1QE2J1DQZ12EH1QEZI1HL10QF1HIEDIQM5EQ_YDQ_BY6CQYQ_1HJY6DQHYDAQA11FQJ51CI1BL1IQ_EB0BOQYBEE2Q2HECQJ51Q_ECCEDQF1EFB1QYIQJ5EK35QJ51OQ21YH10QJEQBEI1QJ516HQ6CFEHJYD_1QZOQJ51Q_EDJY_JQM56BIJQMYDJEDQ60B1HIQYD0QIK_5QYIQYH1QFHED1QJEQZY0Q7EA6D3QY221_JQJEQ01I_1D0QJEQJ516HQB1L1BQEDBOQJEQCYA1QJ51QFEEHQF1EFB1Q211BQJ516HQ6CF1HJ6D1D_1QYBBQJ51QCEH1QA11DBOQQ6QADEMQL1HOQM1BBQJ5YJQM1QYH1QDEJQYBBQ1GKYBQDEHQ_YDQZ1QIEQZKJQ6JQ6IQCOQEF6D6EDQJ5YJQ51QM5EQYLE60IQJ51Q_ECCEDQF1EFB1Q6DQEH01HQDEJQJEQBEI1QJ516HQH1IF1_JQ6IQYIQCK_5QJEQZBYC1QYIQYQ_EMYH0QM5EQ5601IQ56CI1B2Q2HECQ56IQ1D1COQZ1_YKI1Q51Q21YHIQ0121YJQQJ51QEJ51HQ0YOQ6QM1DJQJEQJ51Q2EKDJY6DQYD0Q2EKD0QYQOEKD3QI1HLYDJQ36HBQM5EQ5Y0QI1JQ51HQF6J_51HQEDQJ51QBEM1IJQIJ1FQYD0QBEEA10QYHEKD0QJEQI11Q62QED1QE2Q51HQ_ECFYD6EDIQMYIQYFFHEY_56D3QJEQFBY_1Q6JQEDQ51HQ51Y0Q6QHYDQ0EMDQYD0QBEEA10QYJQ51HQI5YBBQ6Q51BFQOEKQFH1JJOQBYIIQIY60Q6QI51QZBKI510Q011FBOQE5QI6HQI51Q1N_BY6C10QDEQ_1H1CEDOQ6QH1FB610QI51QY07KIJ10Q51HQ51Y0Q31YHQYD0Q6Q51BF10Q51HQI51QJ5YDA10QC1QYD0QYI_1D010QJ51QIJ1FIQQCYOQSXQQ6Q5YL1QCY01QYBBQIEHJIQE2QY_GKY6DJYD_1IQZKJQ5YL1QYIQO1JQ2EKD0QDEQIE_61JOQ6QADEMQDEJQM5YJQYJJHY_J6EDQ6QFEII1IIQ2EHQJ51QF1EFB1QIEQCYDOQE2QJ51CQB6A1QC1QYD0QYJJY_5QJ51CI1BL1IQJEQC1QYD0QJ51DQ6Q211BQIEHHOQM51DQJ51QHEY0QM1QFKHIK1QJE31J51HQ3E1IQEDBOQYQI5EHJQ06IJYD_1Q62QOEKQ6DGK6H1QM5YJQJ51QF1EFB1QYH1QB6A1Q51H1Q6QCKIJQYDIM1HQJ51QIYC1QYIQ1L1HOM51H1QJ51Q5KCYDQHY_1Q6IQZKJQYQCEDEJEDEKIQY22Y6HQCEIJQE2QJ51CQBYZEKHQJ51Q3H1YJ1HQFYHJQE2QJ516HQJ6C1Q2EHQC1H1QIKZI6IJ1D_1QYD0QJ51QI_YDJOQFEHJ6EDQE2Q2H110ECQM56_5QH1CY6DIQJEQJ51CQIEQJHEKZB1IQJ51CQJ5YJQJ51OQKI1Q1L1HOQ1N1HJ6EDQJEQ31JQH60QE2Q6JQE5QJ51Q01IJ6DOQE2QCYDQQZKJQJ51OQYH1QYQH635JQ3EE0QIEHJQE2QF1EFB1Q62Q6QE__YI6EDYBBOQ2EH31JQCOI1B2QYD0QJYA1QFYHJQ6DQJ51Q6DDE_1DJQFB1YIKH1IQM56_5QYH1QDEJQO1JQ2EHZ6001DQJEQJ51QF1YIYDJHOQYD0Q1D7EOQCOI1B2Q2EHQ6DIJYD_1QM6J5Q31DK6D1Q2H110ECQYD0QI6D_1H6JOQHEKD0QYQM1BBQ_EL1H10QJYZB1QEHQYHHYD31QYDQ1N_KHI6EDQEHQYQ0YD_1QEFFEHJKD1BOQYD0QIEQ2EHJ5QYBBQJ56IQFHE0K_1IQYQ3EE0Q1221_JQKFEDQCOQ06IFEI6J6EDQEDBOQ6QCKIJQ2EH31JQJ5YJQJ51H1QB61Q0EHCYDJQM6J56DQC1QIEQCYDOQEJ51HQGKYB6J61IQM56_5QCEKB01HQKI1B1IIBOQYD0QM56_5Q6QYCQEZB6310QJEQA11FQ_YH12KBBOQ_ED_1YB10QY5QJ56IQJ5EK35JQY221_JIQCOQIF6H6JIQ21YH2KBBOQYD0QO1JQJEQZ1QC6IKD01HIJEE0Q6IQJ51Q2YJ1QE2QJ51QB6A1QE2QKIQQYBYIQJ5YJQJ51Q2H61D0QE2QCOQOEKJ5Q6IQ3ED1QYBYIQJ5YJQ6Q1L1HQAD1MQ51HQ6QC635JQIYOQJEQCOI1B2QOEKQYH1QYQ0H1YC1HQJEQI11AQM5YJQ6IQDEJQJEQZ1Q2EKD0Q51H1QZ1BEMQZKJQI51Q5YIQZ11DQC6D1Q6Q5YL1QFEII1II10QJ5YJQ51YHJQJ5YJQDEZB1QIEKBQ6DQM5EI1QFH1I1D_1Q6QI11C10QJEQZ1QCEH1QJ5YDQ6QH1YBBOQMYIQZ1_YKI1Q6QMYIQYBBQJ5YJQ6Q_EKB0QZ1Q3EE0Q51YL1DIQ060QJ51DQYQI6D3B1QFEM1HQE2QCOQIEKBQH1CY6DQKD1N1H_6I10Q6DQ51HQFH1I1D_1Q_EKB0Q6QDEJQ06IFBYOQJEQ6JIQ2KBBQ1NJ1DJQJ5YJQCOIJ1H6EKIQ211B6D3QM6J5QM56_5QCOQ51YHJQ1CZHY_1IQDYJKH1QMYIQDEJQEKHQ6DJ1H_EKHI1QYQF1HF1JKYBQM1ZQE2QJ51Q26D1IJQ1CEJ6EDIQE2QJ51QA11D1IJQM6JQJ51QLYH61J61IQE2QM56_5Q1L1DQ6DQJ516HQL1HOQ1__1DJH6_6JOQZEH1QJ51QIJYCFQE2Q31D6KIQYBYIQJ51Q21MQO1YHIQZOQM56_5QI51QMYIQCOQI1D6EHQZHEK35JQ51HQJEQJ51Q3HYL1QZ12EH1QC1QD1L1HQ_YDQ6Q2EH31JQ51HQ26HCQC6D0QEHQ51HQ51YL1DBOQFYJ61D_1QQYQ21MQ0YOIQY3EQ6QC1JQYQ_1HJY6DQOEKD3QLQQQYQ2HYDAQEF1DQ21BBEMQM6J5QYQCEIJQFB1YI6D3Q_EKDJ1DYD_1Q51Q5YIQ7KIJQB12JQJ51QKD6L1HI6JOQ0E1IQDEJQ011CQ56CI1B2QEL1HM6I1QZKJQZ1B61L1IQ51QADEMIQCEH1QJ5YDQEJ51HQF1EFB1Q51Q5YIQMEHA10Q5YH0QYIQ6Q_YDQF1H_"

alphabet_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
CHARS = []
for ch in alphabet_string:
    CHARS.append(ch)
chars_to_num = {}
num_to_char = {}
for i in range(len(CHARS)):
    chars_to_num[CHARS[i]]=i
    num_to_char[i] = CHARS[i]
print(chars_to_num['E']-chars_to_num['1'])
print(chars_to_num['_']-chars_to_num['Q'])

ENGLISH_DICT = {}


def parse_on_spaces(in_text):
    return in_text.split('_')

def check_english(words_list):
    N = len(words_list)
    count = 0
    for w in words_list:
        if w in words_list:
            count +=1
    return count/N



freq1 = {}
for char in CIPHER:
    if char in freq1.keys():
        freq1[char] += 1
    else:
        freq1[char] = 1
print(freq1)
freq1_list=sorted(freq1.items(),key=itemgetter(1))
freq1_list_bis = [[],[]]
for elem in freq1_list:
    freq1_list_bis[0].append(elem[0])
    freq1_list_bis[1].append(elem[1])
plt.bar(range(len(freq1)),freq1_list_bis[1],align='center')
plt.xticks(range(len(freq1)),freq1_list_bis[0])
#plt.show()

new_text = CIPHER.replace('Q',' ')

words = new_text.split(' ')
words_freq = {}
for w in words:
    if w in words_freq.keys():
        words_freq[w] += 1
    else:
        words_freq[w] = 1
print(words_freq)

words_list = sorted(words_freq.items(),key=itemgetter(1))
words_double_list = [[],[]]
for elem in words_list:
    words_double_list[0].append(elem[0])
    words_double_list[1].append(elem[1])
plt.figure()
plt.bar(range(20),words_double_list[1][-20:],align='center')
plt.xticks(range(20),words_double_list[0][-20:])
plt.show()

#new_text = new_text.replace('1','e')
#new_text = new_text.replace('J','t')
#new_text = new_text.replace('5','h')

#print(new_text)