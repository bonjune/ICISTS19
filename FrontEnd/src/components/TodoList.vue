<template>
    <div>
        <transition-group name="list" tag="ul">
            <li v-for="(todoItem, index) in propsdata" v-bind:key="todoItem.item" class="shadow">
                <i class="checkBtn fas fa-check" v-bind:class="{checkBtnCompleted: todoItem.comp}" v-on:click="toggleComplete(todoItem,index)"></i>
                <!-- 동적으로 t/f 값에 따라 class 변환 -->
                <span v-bind:class="{textCompleted: todoItem.completed}"> {{todoItem.item}} </span>
                <span class="removeBtn" v-on:click="removeTodo(todoItem, index)">
                    <i class="fas fa-trash-alt"></i>
                </span>
            </li>
        </transition-group>
    </div>
</template>

<script>
export default {
    props: ['propsdata'],
    methods:{
        removeTodo:function(todoItem, index){
            this.$emit('removeItem', todoItem, index);
        },
        toggleComplete: function(todoItem, index){
            this.$emit('toggleItem', todoItem, index);
        }
    }
}
</script>

<style>
ul{
    list-style-type: none;
    padding-left: 0px;
    margin-top: 0;
    text-align: left;
}
li{
    display: flex;
    min-height: 50px;
    height: 50px;
    line-height: 50px;
    margin: 0.5rem 0;
    padding: 0 0.9rem;
    background: white;
    border-radius: 5px;
}
.removeBtn{
    margin-left: auto;
    color: #de4343;
}
.checkBtn{
    line-height: 45px;
    color: #62acde;
    margin-left: 5px;
    margin-right: 1rem;
}
.checkBtnCompleted{
    color: #b3adad;
}
.textCompleted{
    text-decoration: line-through;
    color: #b3adad;
}
/* 리스트 트랜지션 */
.list-item {
  display: inline-block;
  margin-right: 10px;
}
.list-enter-active, .list-leave-active {
  transition: 0.5s 0.1s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
</style>
