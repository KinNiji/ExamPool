window.onscroll = function () { sc(); };//当系统滚屏时触发
window.onresize = function () { sc(); };//改变窗口大小时触发
window.onload = function () { sc(); };//页面加载时触发

function sc() {
    var h = document.documentElement.clientHeight;
    $("#page_content").css({ height: h });
}

////页面加载时绑定按钮点击事件
//$(function () {
//    $("#exercise-back").click(function () {
//        refresh();
//    });
//});
////点击按钮调用的方法
//function refresh() {
////    window.location.reload();//刷新当前页面
////    parent.location.reload();//刷新父亲对象（用于框架）--需在iframe框架内使用
////    opener.location.reload();//刷新父窗口对象（用于单开窗口)
////    top.location.reload();//刷新最顶端对象（用于多开窗口）
//}

//$('#exercise-back').bind('click',
//    function(){
//        javascript:location.reload();
//    }
//);