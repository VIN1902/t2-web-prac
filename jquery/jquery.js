$("document").ready(function(){
    $("button").click(function () {
        $("body").css({
            "background-color": "black",
            "color": "white"
        })

        $("p").before("<h3 class='bef'>phele lag gya</h3>")
        let a = $(".bef").html()
        console.log(a)
        $("p").after("<h3 class='aft'>बाद मे लग  गया</h3>")
        let b = $(".aft").text()
        console.log(b)

        // $("input:text").val("Hey there")
        $("input[type='text']").val("Bye Bye")
    })
})