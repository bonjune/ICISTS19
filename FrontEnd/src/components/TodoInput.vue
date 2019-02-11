<template>
    <div class="inputBox shadow">
        <!-- vue 단에서 동적으로 인식 -->
        <input type="text" v-model="newTodoItem" v-on:keyup.enter="addTodo">
        <!-- <button v-on:click="addTodo">add</button> -->
        <span class="addContainer" v-on:click="addTodo">
            <i class="fas fa-plus addBtn"></i>
        </span>
        <modal v-if="showModal" @close="showModal = false">
        <h3 slot="header">
            <i class="fas fa-times closeModalBtn modal-default-button" @click="showModal = false"></i>
            Notification!
        </h3>
        <h3 slot="body">
            한국 가고싶다 엉엉.
        </h3>
        </modal>
    </div>
</template>

<script>
import Modal from './common/Modal.vue'

export default {
    data: function(){
        return {
            newTodoItem: "",
            showModal: false
        }
    },
    methods: {
        addTodo: function(){
            if (this.newTodoItem !== ''){
                // console.log(this.newTodoItem);
                // //저장
                this.$emit('addTodoItem', this.newTodoItem)
                this.clearInput();
            } else{
                this.showModal = !this.showModal;
            }
        },
        clearInput: function(){
            this.newTodoItem = '';
        }
    },
    components: {
        Modal: Modal
    }
}
</script>

<style scoped>
input:focus{
    outline: none;
}
.inputBox{
    background: white;
    height: 50px;
    line-height: 50px;
    border-radius: 5px;
}
.inputBox input{
    border-style: none;
    font-size: 0.9rem;
}
.addContainer{
    float: right;
    background: linear-gradient(to right, #6478fb, #8763fb);
    display: block;
    width: 3rem;
    border-radius: 0 5px 5px 0;
}
.addBtn{
    color:white;
    vertical-align: middle;
}
.closeModalBtn {
    color: #42b983;
}
p.margin {
    margin-top: 0.2px;
    margin-bottom: 2px;
}
</style>
