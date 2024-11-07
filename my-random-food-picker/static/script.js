async function chooseFood() {
   const foodList = document.getElementById('food-list').value;
   const foods = foodList.split(',').map(food => food.trim());
   
   if (foods.length === 0) {
       alert("Please enter some food items!");
       return;
   }

   try {
       const response = await fetch('/choose_food', {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({ foods })
       });
       
       const data = await response.json();
       if (data.chosen_food) {
           document.getElementById('result').innerText = `You should eat: ${data.chosen_food}`;
       }
   } catch (error) {
       alert('Error choosing food!');
   }
}