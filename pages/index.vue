<script setup></script>
<template>
  <main class="mx-6 text-center md:mx-12">
    <header class="flex flex-col items-center pt-24 text-center">
      <h1>Default Font Sizes</h1>
      <p>This is to establish a baseline of responsive fonts</p>
    </header>
    <section class="large-section">
      <header class="my-8 flex justify-center text-center">
        <Icon name="fa6-brands:fedora" class="mr-4 text-5xl" />
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
      <header class="my-8 text-center">
        <h2
          class="bg-gradient-to-r from-fp-blue to-fp-purple bg-clip-text font-extrabold text-transparent"
        >
          Non Heading Text
        </h2>
      </header>
      <div class="mx-auto mb-8">
        <h4>Paragaph Text</h4>
        <p>
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad
          cupiditate expedita odio id laboriosam nesciunt assumenda labore rerum
          nemo ipsa.
        </p>
      </div>
      <div class="my-4 flex flex-wrap justify-center gap-4 lg:gap-8">
        <nav>
          <h4>Ul in Nav</h4>
          <ul>
            <li>one</li>
            <li>two</li>
          </ul>
        </nav>
        <div>
          <h4>Unordered List</h4>
          <ul class="marker:text-2xl marker:text-fp-blue">
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
        <h4 class="mb-4 text-center">Code Blocks</h4>
        <pre>
            <code>
              .example-class {
                font-weight: bold;
                color: rebeccapurple; 
              }
            </code>
            </pre>
      </div>
      <div
        class="my-4 grid w-full grid-cols-2 items-center md:w-1/2 md:grid-cols-4"
      >
        <h4 class="col-span-full mb-2 text-center">Buttons</h4>
        <p class="col-span-full mb-4 text-center">
          In <code>pages/index.vue</code> you can see how the default color and
          it's hover background color are overriden.
        </p>
        <FpBtn>Default</FpBtn>
        <FpBtn color="bg-fp-magenta hover:bg-fp-magenta/[0.6]"
          >bg-magenta</FpBtn
        >
        <FpBtn color="bg-fp-green hover:bg-fp-green/[0.6]">bg-green</FpBtn>
        <FpBtn color="bg-fp-purple hover:bg-fp-purple/[0.6]">bg-purple</FpBtn>
      </div>
    </section>
    <section class="flex flex-col items-center">
      <header class="section-header">
        <h2>Icons</h2>
        <p>
          We are now using the
          <a href="https://github.com/nuxt-modules/icon">Nuxt Icon</a> module
          for our icons.
        </p>
      </header>
      <div class="my-4 flex">
        <div class="mr-8 flex max-w-lg flex-wrap gap-4">
          <p>
            Apply a fontawesome icon using the following syntax
            <em
              >just remember to surround the code in angle brackets, they are
              not being used here otherwise vue would render the icon</em
            >
          </p>
          <pre>
              <code>
                Icon name="fa6-brands:fedora"
              </code>
            </pre>
        </div>
        <div class="mb-8 flex flex-col gap-4 text-5xl md:gap-8">
          <Icon name="fa6-solid:user-secret" />
          <Icon name="fa6-brands:fedora" />
          <Icon name="fa6-regular:chess-rook" />
        </div>
      </div>
    </section>
  </main>
</template>
