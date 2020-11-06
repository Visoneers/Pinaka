// console.log ("hello world")
var updateBtns=document.getElementsByClassName('update-cart')

for (var i=0;i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId =this.Dataset.product
        var action=this.Dataset.action
        console.log('productId:',productId,'action:',action)
    })
}