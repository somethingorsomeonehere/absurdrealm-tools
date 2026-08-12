<template>
  <Layout>
    <template #doc-after>
      <SuggestEdit />
    </template>
  </Layout>
</template>

<script setup>
import DefaultTheme from 'vitepress/theme'
import SuggestEdit from './components/SuggestEdit.vue'

const { Layout } = DefaultTheme
</script>