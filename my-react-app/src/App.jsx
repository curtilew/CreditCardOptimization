import Card from "./Card"
import Button from "./Button";
import Student from "./Students";
import UserGreeting from "./UserGreeting";
import List from "./List";
import ProfilePicture from "./ProfilePicture";
import MyComponent from "./MyComponent";
import Counter from "./Counter";

function App() {

    const fruits = [{id: 1, name:'apple', calories: 95}, 
      {id: 2, name:'orange', calories: 45}, 
      {id: 3, name:'banana', calories: 105}, 
      {id: 4, name:'coconut', calories: 159},
      {id: 5, name:'pineapple', calories: 37}];

    const vegetables = [{id: 6, name:'potatoes', calories: 110}, 
      {id: 7, name:'celery', calories: 15}, 
      {id: 8, name:'carrots', calories: 25}, 
      {id: 9, name:'corn', calories: 63},
      {id: 10, name:'broccoli', calories: 50}];

    return(
      <>
      
      <Card/>
      <Card/>
      <MyComponent />
      <Counter />
      <Button/>
      <ProfilePicture />
      <Student name="Spongebob" age={30} isStudent={true}/>
      <Student name="Patrick" age={42} isStudent={false}/>

      <UserGreeting isLoggedIn={true} username="tman"/>
      <List items={fruits} category="Fruits" />
      <List items={vegetables} category="Vegetables" />
      
      </>
    );
  }

export default App
