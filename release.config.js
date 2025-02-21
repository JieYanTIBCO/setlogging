module.exports = {
  branches: ['main'],
  plugins: [
    '@semantic-release/commit-analyzer',
    '@semantic-release/release-notes-generator',
    '@semantic-release/changelog',
    ['@semantic-release/exec', {
      verifyConditions: [],
      analyzeCommits: [],
      verifyRelease: [],
      generateNotes: [],
      prepare: [
        'hatch version ${nextRelease.version}',
        'git add src/setlogging/__init__.py'
      ],
      publish: [
        'hatch build',
        'twine upload dist/*'
      ],
      success: [],
      fail: []
    }],
    ['@semantic-release/git', {
      assets: ['CHANGELOG.md', 'src/setlogging/__init__.py'],
      message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}'
    }],
    '@semantic-release/github'
  ]
}
