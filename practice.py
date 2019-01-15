if (msg == "//실시간검색어") {

        var data = Utils.getWebText("https://m.search.naver.com/search.naver?query=날씨");

        var data2 = data.split("11~20위</span>");

        var data3 = data2[1].split("DataLab</i>급상승 트래킹");

        var data4 = data3[0].replace(/(<([^>]+)>)/g, "");

        data4 = data4.trim();

        data4 = data4.replace(/  /g, "");
        data4 = data4.replace(/검색추이/g, "");
        data4 = data4.replace(/\n/g, "");


        data4 = data4.replace(/    /g, "\n");
data4 = data4.replace(/  /g, "");
data4 = data4.replace(/\n11/g, "11");
data4 = data4.replace(/\n11/g, " 11. ");
data4 = data4.replace(/\n12/g, " 12. ");
data4 = data4.replace(/\n13/g, " 13. ");
data4 = data4.replace(/\n14/g, " 14. ");
data4 = data4.replace(/\n15/g, " 15. ");
data4 = data4.replace(/\n16/g, " 16. ");
data4 = data4.replace(/\n17/g, " 17. ");
data4 = data4.replace(/\n18/g, " 18. ");
data4 = data4.replace(/\n19/g, " 19. ");
data4 = data4.replace(/\n20/g, " 20. ");
data4 = data4.replace(/\n1/g, " 1. ");
data4 = data4.replace(/\n2/g, " 2. ");
data4 = data4.replace(/\n3/g, " 3. ");
data4 = data4.replace(/\n4/g, " 4. ");
data4 = data4.replace(/\n5/g, " 5. ");
data4 = data4.replace(/\n6/g, " 6. ");
data4 = data4.replace(/\n7/g, " 7. ");
data4 = data4.replace(/\n8/g, " 8. ");
data4 = data4.replace(/\n9/g, " 9. ");
data4 = data4.replace(/\n10/g, " 10. ");


        replier.reply("[실시간 급상승]\n" + data4);

    }