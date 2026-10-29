import type { CollectionEntry } from 'astro:content'

export const VOID_TAG = 'void'

/**
 * Trim, drop empty entries and de-duplicate tags.
 */
export function normalizeTags(tags?: string[] | null): string[] {
  return [...new Set((tags ?? []).map((tag) => tag.trim()).filter(Boolean))]
}

/**
 * Tags shown in the UI. Posts without tags fall back to the "void" tag.
 */
export function displayTags(tags?: string[] | null): string[] {
  const list = normalizeTags(tags)
  return list.length > 0 ? list : [VOID_TAG]
}

/**
 * Link to the tags page with the tag already selected.
 */
export function tagHref(tag: string): string {
  return `/tags/#${encodeURIComponent(tag)}`
}

export interface TagGroup {
  name: string
  posts: CollectionEntry<'posts'>[]
}

/**
 * Build the tag -> posts index used by the tags page.
 */
export function groupPostsByTag(posts: CollectionEntry<'posts'>[]): TagGroup[] {
  const index = new Map<string, CollectionEntry<'posts'>[]>()

  for (const post of posts) {
    for (const tag of displayTags(post.data.tags)) {
      const group = index.get(tag)
      if (group) {
        group.push(post)
      } else {
        index.set(tag, [post])
      }
    }
  }

  return [...index.entries()]
    .map(([name, groupedPosts]) => ({ name, posts: groupedPosts }))
    .sort((a, b) => a.name.localeCompare(b.name, 'zh-CN'))
}
