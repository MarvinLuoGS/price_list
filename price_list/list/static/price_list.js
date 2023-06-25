let allRadios = document.querySelectorAll('input[type=radio]')
    function submitForm() {
        let form = document.getElementById('form');
        if (form.reportValidity()) {
            let switchingPoint = document.getElementById('id_switching_point');
            let consistency = document.getElementById('id_consistency')
            let left_sum = document.getElementById('id_left_sum')
            let right_sum = document.getElementById('id_right_sum')
            let choice_list = document.getElementById('id_choice_list')

            let allChoicesAreOnLeft = true;
            for (let radio of allRadios) {
                if (radio.value === '1' && radio.checked) {
                    switchingPoint.value = radio.dataset.amount;
                    allChoicesAreOnLeft = false;
                    break;
                }
            }
            if (allChoicesAreOnLeft) {
                // '9999' represents the valueInput if the user didn't click the right side for any choice
                // it means their switching point is off the scale. you can change 9999 to some other valueInput
                // that is larger than any right-hand-side choice.
                switchingPoint.value = 9999;
            }
        
            let temp_consistency = true;
            for (let i = 0; i < allRadios.length - 1; i++) {
                if (allRadios[i].value === '1' && allRadios[i+1].value === '0' && allRadios[i].checked && allRadios[i+1].checked ) {
                    temp_consistency = false;
                    break;
                }
            }
            consistency.value = temp_consistency;
            left_sum.value = leftAnswers;
            right_sum.value = rightAnswers;
            answers_list = Object.values(answers);
            choice_list.value = answers_list;
            form.submit();
        }
    }

   
// calculate the number of rows choosing left and right,respectively
let leftAnswers = 0;
let rightAnswers = 0;
let answers = {};

function handleClick(radio) {
  let qNumber = radio.name;  // Extract question number from name="q1"
  
  if (answers[qNumber] == radio.value) return;  // Already selected
  
  if (answers[qNumber] == '0') leftAnswers--;   // Decrement previous answer
  else if (answers[qNumber] == '1') rightAnswers--;   
  
  if (radio.value == '0') leftAnswers++;          // Increment new answer 
  else rightAnswers++;
  
  answers[qNumber] = radio.value;  // Update selected answer
  document.getElementById('results').innerHTML = `Number of Option A: ${leftAnswers}, Number of Option B: ${rightAnswers}`; 
}
