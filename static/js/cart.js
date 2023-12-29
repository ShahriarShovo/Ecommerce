// console.log('hello')
// var add_to_cart_btn = document.getElementsByClassName('update-cart')



// for (var i=0; i<add_to_cart_btn.length; i++){
//     add_to_cart_btn[i].addEventListener('click', function(){

//         var product_id = dataset.product
//         var action = dataset.action

//         console.log('product id ',product_id)
//         console.log('action', action)


//     })
// }


function increaseCount(a, b) {
    var input = b.previousElementSibling;
    var value = parseInt(input.value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    input.value = value;
  }
  
function decreaseCount(a, b) {
    var input = b.nextElementSibling;
    var value = parseInt(input.value, 10);
    if (value > 1) {
      value = isNaN(value) ? 0 : value;
      value--;
      input.value = value;
    }
  }

  function get_color_name(color){
    console.log(color)
    window.location.href = window.location.pathname + `?color=${color}`
  }


function get_size_name(size){
    console.log(size)
    window.location.href = window.location.pathname + `?size=${size}`
  }



