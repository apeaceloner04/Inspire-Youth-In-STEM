console.log("button clicked")
document.getElementsById("confirm_btn").onclick=function check()
{
    var age=document.getElementById("age").value;
    if(age<18)
    {var x="you cant get in";
console.log("good job")}
    else
    {var x="you can get in";}
    document.getElementById("get_in").innerHTML=x;

}


