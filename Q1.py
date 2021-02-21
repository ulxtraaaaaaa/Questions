@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  embed = discord.Embed(color=discord.Colour.from_rgb(0,255,0),description=f"**{member} Has Been Banned**\nReason: `{reason}`")
  embed.set_author(name=member,icon_url=member.avatar_url)
  embed.set_footer(text=f"Responsible: {ctx.author}")
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,title="Missing Required Argument!",description="**Please Input A Valid Member.**")
    await ctx.send(embed=embed)
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),timestamp=ctx.message.created_at,title="Missing Permissions!",description="**You Are Missing The Proper Permissions To Execute This Command.**")
    await ctx.send(embed=embed)
