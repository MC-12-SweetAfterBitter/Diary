    function paging(totalData, currentPage) {
        const dataPerPage = 10;
        const pageCount = 5;

        // console.log("currentPage : " + currentPage);
        // console.log("totalData : " + totalData);
        const totalPage = Math.ceil(totalData / dataPerPage);    // 총 페이지 수
        const pageGroup = Math.ceil(currentPage / pageCount);    // 페이지 그룹

        // console.log("pageGroup : " + pageGroup);
        // console.log("totalPage : " + totalPage);

        let last = pageGroup * pageCount;    // 화면에 보여질 마지막 페이지 번호
        if (last > totalPage)
            last = totalPage;
        let first = last - (pageCount - 1);    // 화면에 보여질 첫번째 페이지 번호
        const next = last + 1;
        const prev = first - 1;

        // console.log("last : " + last);
        // console.log("first : " + first);
        // console.log("next : " + next);
        // console.log("prev : " + prev);

        if (totalPage < 1) {
            first = last;
        }
        const pages = $("#pages");
        pages.empty();
        if (first > 5) {
            pages.append("<li class=\"pagination-item\">" +
                "<a onclick=\"GetTarget(" + (prev) + ");\" style='margin-left: 2px'>prev</a></li>");
        }
        for (let j = first; j <= last; j++) {
            if (currentPage === (j)) {
                pages.append("<li class=\"pagination-item\">" +
                    "<a class='active' onclick=\"GetTarget(" + (j) + ");\" style='margin-left: 2px'>" + (j) + "</a></li>");
            } else if (j > 0) {
                pages.append("<li class=\"pagination-item\">" +
                    "<a onclick=\"GetTarget(" + (j) + ");\" style='margin-left: 2px'>" + (j) + "</a></li>");
            }
        }
        if (next > 5 && next < totalPage) {
            pages.append("<li class=\"pagination-item\">" +
                "<a onclick=\"GetTarget(" + (next) + ");\" style='margin-left: 2px'>next</a></li>");
        }
    }
