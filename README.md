# Preface

Whether it's realized or not, most people are log(wealth) maximalists, contrary to maximizing linear wealth. What does this mean? Effectively, we *dislike* the risk of loss more than we *like* potential for gain, increasingly so at the progressive ends of each.

For example:

Let's say you have a net worth of $20k. Now, it's your lucky day; you are presented with a +EV bet.
Someone offers to flip a coin. If it lands on heads, you give them $10k. If it lands on tails, they give you $12k.

You have 50/50 odds with an asymmetric risk:reward bet in your favor. You should take your chances, right? Probably not.

A linear wealth maximalist would accept this bet, while a log wealth maximalist would reject it. For the latter, risk:reward is assessed logarithmically.

In the scenario of heads, your NW multiplier is .5 ((20k-10k)/20k)).
In the scenario of tails, your NW multiplier is 1.6 ((20k+12k)/20k)).

So, you can then take the natural log of both of these values. ln(.5) = -.69 ; ln(1.6) = .47

For a log wealth maximalist, only now can you take these values and assess linearly.

You have 50/50 odds with a win value of .47 and a loss value of -.69. Is this a bet you should take? No, it has a negative log expected value.


# Okay, so why does this matter? 

The concept of log wealth maximization sets the stage for an existing problem within the investment domain of which there are not practical solutions for, especially for retail investors.

Most people realize that it's a good idea to hold exposure in assets with expected *growth*, like equities. However, most people are also cautious about limiting their exposure, because they are intuitive log wealth maximalists, even if they don't explicitly realize it. 

So, how might one go about maintaining the maximum amount of exposure in growth assets while holding asymmetric averseness to downside risk? Well, the easiest and most common way to do this is simply limiting the amount invested, and keeping the rest in low risk credit markets or even USD.

But is there a more effective way of doing this? Yes, by using a cool instrument that is traditionally known as an options contract.

# So what is the problem?

The barrier of entry for correctly using options contracts as an effective hedging tool is high. As of now, the most common use of options contracts for retail investors is high leverage gambling.

# Then what is the solution?

My proposition to build a market platform with a completely different way of framing options contracts. Currently, options are bought and sold on an esoteric-looking grid of varying expiration dates, strike prices, and type, ie. call or put. If we refer to the number of expiry choices as D and the number of strike price choices as S, we can say that there are 2 * D * S different markets within one options book. If an options book has 15 choices for expiry dates and each 10 strike price choices, that is 2 * (15) * (10) = ***300*** distinct markets for one book.

*How in the world is the typical retail investor expected to navigate this properly?*

My proposed solution is to condense traditional options into a simple, intuitive interface that supports the most useful actual hedging mechanism that they can represent, ***insurance***. More specifically, ***investors insurance***.

# What would this look like?

Let's look at how insurance works in other markets, for example, a simplified version of home insurance.

You own a home with some market value. You want (or are required, but let's ignore that) protection in the event of a black swan event like a hurricane. Otherwise, you face the risk financial ruin if something destroys your home.

So you request a quote from an insurance company. Assuming you default to replacement cost coverage, you only have one main decision:

How high of a deductible do you opt for? You know the deductible is inversely determinant of your premiums, so you want to go as high as you can, up to the point at which out-of-pocket costs above this level of deductible would begin affecting your financial wellbeing at an *increasingly* negative rate.


So let's transpose how this concept of *insurance* can be applied to investments.

Reverting to the first example, you have a net worth of $20k. You want as much possible exposure to growth investments but also determine that if your portfolio drops below a certain threshold, let's say $5k, cumulative losses below that will affect your wellbeing at an *increasingly* negative rate.

So what you have done here is figured out your optimal investment insurance deductible; $15k (20k-5k).

With traditional options, you could purchase a *synthetic* insurance policy on your portfolio by purchasing X put option contracts at Y strike price on an indefinite cycle of expiries. If we pretend your portfolio holds only one asset and 1 contract = 1 unit, X is (((C*(1+(P/U))/Y)) where C is the point of inflection of your wellbeing as a function of portfolio value, P is the premium at given strike price and U is the underlying spot price of the asset. Y is ((C/V)*U)) where V is the current portfolio value of in this case, one asset.

Point being, the only two variable inputs of an investor needed to determine the optimal hedging contract (policy) is (1) Portfolio contents and (2) Optimal deductible i.e. point of inflection on wellbeing curve as a function of net worth.

We can therefore construct a market for investors insurance in the same way that traditional insurance markets function. The investor can request a quote on this proposed market by indicating only two pieces of information. This information can then be substituted into the introduced formulas to convert the information into a traditional put option solicitation to be listed on an open marketplace of flexible options contracts. The rest is then handled by the competitive nature of free markets. Options writers can freely assess the transposed contract solicition and provide competitive bids at which premiums they will offer a counterparty to the specifications of the contract solicited by the investor.
