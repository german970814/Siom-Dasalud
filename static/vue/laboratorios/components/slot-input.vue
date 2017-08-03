<template lang="html">
    <div class="">
        <slot></slot>
        <div v-show="false">
          <slot name="input"></slot>
        </div>
    </div>
</template>

<script>
export default {
}
</script>

<style lang="css">
</style>
