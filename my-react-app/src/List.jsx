
function List(props) {

    const category = props.category
    const itemList = props.items;

    // fruits.sort((a, b) => a.name.localeCompare(b.name));
    const listItems = itemList.map(item => <li key={item.id}>
                                                {item.name}: &nbsp; 
                                                <b>{item.calories}</b></li>)

    return(<>
            <h3 className="list-category">{category}</h3>
            <ol className="list-items">{listItems}</ol>
            </>);
}

List.defaultProps = {
    category: "Category",
}

export default List