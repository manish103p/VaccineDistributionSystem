function validateRegistration(){
    var letters = /^[A-Za-z]+$/;
    console.log("hi");
    if( document.registerForVaccinationForm.name.value == "" ) {
      document.getElementById('signupwarningDiv').innerHTML = "***Name cannot be Blank***";
      document.registerForVaccinationForm.name.focus() ;
      return false;
    }
    if( !/^[A-Za-z\s]+$/.test(document.registerForVaccinationForm.name.value) ) {
      document.getElementById('signupwarningDiv').innerHTML = "***Name can only Contain Alphabets and Space***";
      document.registerForVaccinationForm.name.focus() ;
      return false;
    }

    if( document.registerForVaccinationForm.aadharNumber.value == "" ) {
        document.getElementById('signupwarningDiv').innerHTML = "***Aadhar Number Cannot be Blank***";
        document.registerForVaccinationForm.aadharNumber.focus() ;
        return false;
    }
    if( document.registerForVaccinationForm.aadharNumber.value.length != 16 ){
        document.getElementById('signupwarningDiv').innerHTML = "***Aadhar Number Must be 16 Digits***";
        document.registerForVaccinationForm.aadharNumber.focus() ;
        return false;
    }

    if( document.registerForVaccinationForm.contactNumber.value == "" ) {
      document.getElementById('signupwarningDiv').innerHTML = "***Mobile Number Cannot be Blank***";
      document.registerForVaccinationForm.contactNumber.focus() ;
      return false;
    }
    if( document.registerForVaccinationForm.contactNumber.value.length != 10 ){
      document.getElementById('signupwarningDiv').innerHTML = "***Mobile Number Must be 10 Digits***";
      document.registerForVaccinationForm.contactNumber.focus() ;
      return false;
    }

return true;
}