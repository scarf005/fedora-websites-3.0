<script setup></script>
<template>
  <main class="mx-6 md:mx-12">
    <header class="text-center my-4 flex flex-col items-center">
      <h1>Default Font Sizes</h1>
      <p>This is to establish a baseline of responsive fonts</p>
    </header>
    <section class="large-section">
      <header class="section-header flex">
        <font-awesome-icon icon="fab fa-fedora" class="text-5xl mr-4" />
        <h2>Heading Text</h2>
      </header>
      <h1>An H1 Title</h1>
      <h2>An H2 Title</h2>
      <h3>An H3 Title</h3>
      <h4>An H4 Title</h4>
      <h5>An H5 Title</h5>
    </section>
    <section class="large-section">
      <header class="section-header">
        <h2>Non Heading Text</h2>
      </header>
      <div class="mb-2">
        <h4>Paragaph Text</h4>
        <p>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad
          cupiditate expedita odio id laboriosam nesciunt assumenda labore rerum
          nemo ipsa.
        </p>
      </div>
      <div class="my-4 flex flex-wrap gap-4 lg:gap-8 justify-center">
        <nav>
          <h4>Ul in Nav</h4>
          <ul>
            <li>one</li>
            <li>two</li>
          </ul>
        </nav>
        <div>
          <h4>Unordered List</h4>
          <ul class="marker:text-blue marker:text-2xl">
            <li>An item</li>
            <li>An item</li>
            <li>An item</li>
          </ul>
        </div>
        <div>
          <h4>Ordered List</h4>
          <ol>
            <li>An item</li>
            <li>An item</li>
            <li>An item</li>
          </ol>
        </div>
        <div>
          <dl>
            <dt>A Term</dt>
            <dd>Lorem ipsum dolor sit amet consectetur adipisicing elit.</dd>
            <dt>A Term</dt>
            <dd>Lorem ipsum dolor sit amet consectetur adipisicing elit.</dd>
            <dt>A Term</dt>
            <dd>Lorem ipsum dolor sit amet consectetur adipisicing elit.</dd>
          </dl>
        </div>
      </div>
    </section>
    <section class="large-section flex flex-col items-center">
      <header class="section-header">
        <h2>Code Blocks and Buttons</h2>
      </header>
      <div class="my-4">
        <h4>Code Blocks</h4>
        <pre>
          <code>
            .example-class {
              font-weight: bold;
              color: rebeccapurple; 
            }
          </code>
          </pre>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 w-full md:w-1/2 my-4">
        <h4 class="col-span-full text-center">Buttons</h4>
        <button class="w-fit">Button 1</button>
        <button class="w-fit">Button 2</button>
        <button class="w-fit">Button 3</button>
        <button class="w-fit">Button 4</button>
      </div>
    </section>
    <section class="flex flex-col items-center">
      <header class="section-header">
        <h2>Icons</h2>
        <p>
          Font Awesome 6 icons are hosted in the
          <code>assets/icons/</code> directory. They are read from the nuxt
          module <code>nuxt-icons</code> and can be implemented using PascalCase
          as seen in the following code block.
        </p>
      </header>
      <div>
        <div class="flex justify-around">
          <font-awesome-icon icon="fa-solid fa-user-secret" />
        </div>
      </div>
    </section>
  </main>
</template>

<style lang="postcss">
/* We can still use our own classes in the template and apply tailwind styles down here. This keeps the inline code a bit cleaner and looks great when you use vscodes sfc split editors  */
.large-section {
  @apply my-8 flex flex-col;
}

.section-header {
  @apply mb-4 text-center;
}
</style>
