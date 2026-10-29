import { glob } from 'astro/loaders'
import { defineCollection } from 'astro:content'
import { z } from 'astro/zod'

const posts = defineCollection({
  // Load Markdown and MDX files in the `src/content/posts/` directory.
  loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
  // Type-check frontmatter using a schema
  schema: () =>
    z.object({
      title: z.string(),
      subtitle: z.string().optional(),
      // Transform string to Date object
      pubDate: z.coerce.date(),
      image: z.string().optional(),
      // Free-form tags; an empty list is rendered as the "void" tag.
      tags: z
        .array(z.string())
        .nullish()
        .transform((value) => (value ?? []).map((tag) => tag.trim()).filter(Boolean))
        .default([])
    })
})

const about = defineCollection({
  // Load Markdown files in the `src/content/about/` directory.
  loader: glob({ base: './src/content/about', pattern: '**/*.md' }),
  // Type-check frontmatter using a schema
  schema: z.object({})
})

export const collections = { posts, about }
