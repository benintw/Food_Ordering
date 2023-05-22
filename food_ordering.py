import random
import streamlit as st


def choose_restaurant(restaurants: int) -> int:
    num_restaurants: int = int(restaurants)
    return random.choice(list(range(1, num_restaurants + 1)))


def choose_menu_items(num_menu_items, num_items) -> list[str]:
    menu_items: list[str] = [f"餐點 {i}" for i in range(1, num_menu_items + 1)]
    if num_items <= num_menu_items:
        return random.sample(menu_items, num_items)
    else:
        # Repeat menu items to match the required number of items
        repeated_menu_items = menu_items * ((num_items // num_menu_items) + 1)
        return random.sample(repeated_menu_items, num_items)


def main():
    st.text("40943229S 武氏夢常")
    st.write("---")
    st.title("外賣決定骰子機")

    # 選擇外送平台
    app_var: str = st.radio("選擇外賣APP：", ("UberEats", "FoodPanda"))

    # 輸入目前有幾間餐廳供應
    num_restaurants: str = st.number_input("餐廳數量：", value=1, min_value=1, step=1)

    # 隨機選一家餐廳
    chosen_restaurant: int = choose_restaurant(num_restaurants)

    # 輸入抽到的該餐廳有幾樣餐點
    num_menu_items: str = st.number_input(f"該餐廳的餐點數量：", value=1, min_value=1, step=1)

    # 輸入總共要點幾樣餐點
    num_choices: str = st.number_input("要點幾份餐點? 數量:", value=1, min_value=1, step=1)

    chosen_items = choose_menu_items(num_menu_items, num_choices)

    # Generate choice button
    if st.button("產生結果"):
        message = f"外賣決定骰子機的結果為:\n\n使用 {app_var}，選擇第 {chosen_restaurant} 間餐廳，所選的餐點有：\n\n"
        message += ",\n\n".join(chosen_items)

        st.success(message)


if __name__ == "__main__":
    main()
