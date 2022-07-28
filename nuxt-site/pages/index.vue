<script setup></script>
<template>
  <main class="mx-6 md:mx-12">
    <header class="text-center my-4 flex flex-col items-center">
      <h1>Default Font Sizes</h1>
      <p>This is to establish a baseline of responsive fonts</p>
    </header>
    <section class="large-section">
      <header class="section-header flex mx-auto">
        <font-awesome-icon icon="fab fa-fedora" class="text-5xl mr-4" />
        <h2>Heading Text</h2>
      </header>
      <div class="mx-auto">
        <h1>An H1 Title</h1>
        <h2>An H2 Title</h2>
        <h3>An H3 Title</h3>
        <h4>An H4 Title</h4>
        <h5>An H5 Title</h5>
      </div>
    </section>
    <section class="large-section">
      <header class="section-header">
        <h2>Non Heading Text</h2>
      </header>
      <div class="mb-8 mx-auto">
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
        <h4 class="text-center mb-4">Code Blocks</h4>
        <pre>
          <code>
            .example-class {
              font-weight: bold;
              color: rebeccapurple; 
            }
          </code>
          </pre>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 w-full md:w-1/2 my-4 items-center">
        <h4 class="col-span-full text-center mb-2">Buttons</h4>
        <p class="col-span-full text-center mb-4">In <code>pages/index.vue</code> you can see how the default color and
          it's hover background color are overriden.</p>
        <button class="w-fit my-2">Default</button>
        <button class="w-fit my-2 bg-magenta hover:bg-magenta/[0.6]">bg-magenta</button>
        <button class="w-fit my-2 bg-green hover:bg-green/[0.6]">bg-green</button>
        <button class="w-fit my-2 bg-purple hover:bg-purple/[0.6]">bg-purple</button>
      </div>
    </section>
    <section class="flex flex-col items-center">
      <header class="section-header">
        <h2>Icons</h2>
        <p>
          Font Awesome Icons are hosted through the <a
            href="https://fontawesome.com/docs/web/use-with/vue/use-with">Font Awesome Nuxt Plugin</a>. It is configured
          in the <code>~/plugins/fontawesome.js</code> file.
        </p>
      </header>
      <div class="flex my-4">
        <div class="flex flex-wrap gap-4 max-w-lg mr-8">
          <p><em>Apply a fontawesome icon using this syntax (just remember to use proper brackets, they are not being
              used
              here otherwise vue would render the icon)</em></p>
          <pre>
            <code>
              font-awesome-icon icon="fa-solid fa-bars"
            </code>
          </pre>
        </div>
        <div class="flex flex-col gap-4 md:gap-8 text-5xl mb-8">
          <font-awesome-icon icon="fa-solid fa-user-secret" />
          <font-awesome-icon icon="fa-brands fa-fedora" />
          <font-awesome-icon icon="fa-regular fa-chess-rook" />
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
