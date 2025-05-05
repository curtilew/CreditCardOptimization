import Card from "./Card"
import Button from "./Button";
import Student from "./Students";
import UserGreeting from "./UserGreeting";

function App() {
    return(
      <>
      <Card/>
      <Card/>
      <Button/>
      <Student name="Spongebob" age={30} isStudent={true}/>
      <Student name="Patrick" age={42} isStudent={false}/>

      <UserGreeting isLoggedIn={true} username="tman"/>
      </>
    );
  }

export default App
