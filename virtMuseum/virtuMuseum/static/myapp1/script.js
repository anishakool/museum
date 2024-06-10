'use strict';
// $('#cityGeroi').on('change', function (e) {
//     $('select option').prop('disabled', false);
//     var optionSelected = $("option:selected", this);
//     var valueSelected = this.value;    
//     alert(valueSelected);
//     $("select option:contains('" + valueSelected + "')").attr("disabled","disabled");
// });
$(function(){
    $("select").on("change", function () {
        var valueSelected = this.value.slice(1, -1).split(','); 
        //ar valueSelected = this.value; 
        // console.log(valueSelected);
        
        //$('.smallGeroiImg').attr("static/image/" + valueSelected[2].slice(2, -1));
        
        $('.smallGeroi').html(valueSelected[0].slice(1, -1));
        $('.smallGeroiDesc').html(valueSelected[1].slice(2, -1));
        document.getElementById("smallGeroiImg").src="static/image/" + valueSelected[2].slice(2, -1);
  });
});
